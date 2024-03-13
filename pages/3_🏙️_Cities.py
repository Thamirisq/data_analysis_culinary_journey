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


#import file
df = pd.read_csv('zomato.csv')
df1 = df.copy()

# cleaning file
df1 = df1.drop_duplicates()
df1 = df1.dropna()
df1['City'] = df1['City'].str.strip()
df1['Restaurant Name'] = df1['Restaurant Name'].str.strip()

# colums country name creation
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

# Column 'Cuisines' adjusted to one information by row.
colunas = df1['Cuisines'].str.split(',',expand=True)[0]
df1['Cuisines'] = colunas

#=================================================================================================================

#  side bar logo
image_path = 'logo.png'
image = Image.open(image_path) 

col1, col2 = st.sidebar.columns([1, 2])
with col1:
    st.image("logo.png", width=70)
with col2:
	st.write("# Culinary Journey")

st.sidebar.write('### Filters options')

#  country filters with pre selection.

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

#  page title

st.header('Cities overview 🏙️')


#   bar chart with top 10 cities with more restaurants

df_aux = df1.loc[:,['Restaurant ID','City', 'Country Name']].groupby(['City','Country Name']).count().reset_index().sort_values('Restaurant ID',ascending=False)
fig01 = px.bar(df_aux[0:10], x='City', y='Restaurant ID', labels={'City':'Cities','Restaurant ID':'restaurants quantity'}, title= "Top 10 cities with more resgistered restaurants",text_auto=True, color='Country Name')
st.plotly_chart(fig01, use_container_width = True)

#colums creation
col1,col2 = st.columns(2)


with col1:
# selecting cities with rating over 4.
	df1_aux = df1.loc[:,['City', 'Aggregate rating','Country Name']]
	restaurante_media_alta = df1_aux.loc[df1_aux['Aggregate rating']>4.0,:].groupby(['City','Country Name']).count().reset_index().sort_values('Aggregate rating', ascending=False)
# bar chart
	fig02 = px.bar(restaurante_media_alta[0:7], x='City', y='Aggregate rating', labels= {'City': 'Cities','Aggregate rating': 'Restaurant quantity'} , title= "Top 7 cities with avarage over 4", text_auto=True, color='Country Name')
	st.plotly_chart(fig02, use_container_width = True)

with col2:
    
# selecting cities with rating under 2,5.
    df1_aux = df1.loc[:,['City', 'Aggregate rating','Country Name']]
    restaurante_media_alta = df1_aux.loc[df1_aux['Aggregate rating']<2.5,:].groupby(['City','Country Name']).count().sort_values('Aggregate rating', ascending=False).reset_index()
    fig02 = px.bar(restaurante_media_alta[0:7], x='City', y='Aggregate rating', labels= {'City': 'Cities','Aggregate rating': 'Restaurant quantity'} , title= "Top 7 cities with avarage below 2.5", text_auto=True, color='Country Name')
    st.plotly_chart(fig02, use_container_width = True)
# selecting data to chart of top 10 cities with more cuisine types.
culinaria_unica = df1.loc[:,['Cuisines', 'Country Name','City']].groupby(['City','Country Name']).count().sort_values('Cuisines',ascending=False)
culi_cidade = df1.loc[:,['City', 'Cuisines', 'Country Name']].drop_duplicates()
result = culi_cidade.groupby(['City', 'Country Name']).count().sort_values('Cuisines', ascending=False).reset_index()
# chart of top 10 cities with more cuisine types.  
fig04 = px.bar(result[0:10], x='City', y = 'Cuisines', title = 'Top 10 cities with diferent Cuisines type', text_auto=True, color = 'Country Name')
st.plotly_chart(fig04, use_container_width = True)
               
	