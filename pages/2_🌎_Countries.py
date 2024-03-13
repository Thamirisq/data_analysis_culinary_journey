# imported libraries
import pandas as pd
import numpy as np

from PIL import Image

from folium.plugins import MarkerCluster
import folium
import matplotlib.pyplot as plt
import plotly.express as px
import matplotlib as mp

import streamlit as st
from streamlit_folium import st_folium


# files imported
df = pd.read_csv('zomato.csv')
df1 = df.copy()

# file cleaning
df1 = df1.drop_duplicates()
df1 = df1.dropna()

# creation of column country to names, not numbers.
countries = {
1: "India",
14: "Australia",
30: "Brazil",
37: "Canada",
94: "Indonesia",
148: "New Zeland",
162: "Philippines",
166: "Qatar",
184: "Singapure",
189: "South Africa",
191: "Sri Lanka",
208: "Turkey",
214: "United Arab Emirates",
215: "England",
216: "United States of America",
}

df1['Country Name'] = df1['Country Code']
linhas_selecionadas = df1['Country Name'].replace(countries.keys(), countries.values())
df1['Country Name'] = linhas_selecionadas

# adjust column 'Cuisines' to get only one information per row.
colunas = df1['Cuisines'].str.split(',',expand=True)[0]
df1['Cuisines'] = colunas


#===============================================================================================================

# Sidebar logo
image_path = 'logo.png'
image = Image.open(image_path) 

col1, col2 = st.sidebar.columns([1, 2])
with col1:
    st.image("logo.png", width=70)
with col2:
	st.write("# Culinary Journey")

st.sidebar.write('### Filters options')

# Country filters in sidebar with pre selection.
country_options = st.sidebar.multiselect(
    'Countries', 
        ['Philippines', 'Brazil', 'Australia', 'United States of America',
       'Canada', 'Singapure', 'United Arab Emirates', 'India',
       'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa',
       'Sri Lanka', 'Turkey'], 
        default= ['Brazil','England','Qatar', 'South Africa', 'Canada','Australia']  
)

linhas_selecionadas = df1['Country Name'].isin(country_options)
df1 = df1.loc[linhas_selecionadas, :]

# Currency type filters in sidebar with pre selection.
currency_type = st.sidebar.multiselect('Currency',
                               ['Botswana Pula(P)', 'Brazilian Real(R$)', 'Dollar($)',
       'Emirati Diram(AED)', 'Indian Rupees(Rs.)',
       'Indonesian Rupiah(IDR)', 'NewZealand($)', 'Pounds(£)',
       'Qatari Rial(QR)', 'Rand(R)', 'Sri Lankan Rupee(LKR)',
       'Turkish Lira(TL)'], default=['Brazilian Real(R$)', 'Dollar($)',
                                     'Pounds(£)','Qatari Rial(QR)', 'Rand(R)'])

linhas_selecionadas2 = df1['Currency']. isin(currency_type)
df1 = df1.loc[ linhas_selecionadas2, : ] 

# Page title
st.header('Country overview 🌍')

# country chart
df_aux = df1.loc[:,['Restaurant ID', 'Country Name']].groupby('Country Name').nunique().reset_index().sort_values('Restaurant ID',ascending=False)
fig01 = px.bar(df_aux, x='Country Name', y='Restaurant ID', title= "Number of registered restaurants per country",labels={'Country Name':'Country name','Restaurant ID':'Restaurants quantity'}, text_auto=True)
st.plotly_chart(fig01, use_container_width = True)

# city per country chart
cidades_unicas = df1.loc[:, ['City', 'Country Name']].drop_duplicates()
df_aux = cidades_unicas.groupby('Country Name').count().sort_values('City',ascending=False).reset_index()
fig02 = px.bar(df_aux, x='Country Name', y='City',labels={'Country Name':'Countries','City':'Cities quantity'}, title= "Number of cities registered by country", text_auto=True)
st.plotly_chart(fig02, use_container_width = True)


# two colums creation to information side by side
col1,col2 = st.columns(2)

# avarage votes chart per country
with col1:
	df_aux = df1.loc[:, ['Votes', 'Country Name']].groupby('Country Name').mean().reset_index()
	df_aux['Votes'] = round(df_aux['Votes'],2)  # Arredondando a coluna 'Votes'
	df_aux = df_aux.sort_values('Votes', ascending=False)
	fig03 = px.bar(df_aux, x='Country Name', y='Votes',labels={'Country Name':'Countries','Votes':'Avarage Votes'}, title= "Average number of reviews per country", text_auto=True)
	st.plotly_chart(fig03, use_container_width = True)

# price avarage chart for two per country 
with col2:
	df_aux = df1.loc[:,['Average Cost for two', 'Country Name']].groupby('Country Name').mean().reset_index()
	df_aux['Average Cost for two'] = round(df_aux['Average Cost for two'],2) #arredondando a coluna 'Average Cost for two'
	df_aux = df_aux.sort_values('Average Cost for two',ascending=False)
	fig04 = px.bar(df_aux, x='Country Name', y='Average Cost for two',labels={'Country Name':'Countries','Average Cost for two':'Average price'}, title= "Average meal price for two", text_auto=True)
	st.plotly_chart(fig04, use_container_width = True)

