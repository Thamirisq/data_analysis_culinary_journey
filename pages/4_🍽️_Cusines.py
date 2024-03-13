import numpy as np
import pandas as pd
from PIL import Image

import matplotlib.pyplot as plt
import plotly.express as px
import matplotlib as mp

import streamlit as st
from streamlit_folium import st_folium

#  file importing
df = pd.read_csv('zomato.csv')
df1 = df.copy()

# file cleaning
df1 = df1.drop_duplicates()
df1 = df1.dropna()

#  adding order column
lista = list(range(0, 6929))
df1['lista'] = lista

#   colums country name creation
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

# Sidebar logo

image_path = 'logo.png'
image = Image.open(image_path) 

col1, col2 = st.sidebar.columns([1, 2])
with col1:
    st.image("logo.png", width=70)
with col2:
	st.write("# Culinary Journey")

st.sidebar.write('### Filters options')

# slider filter:

data_slider = st.sidebar.slider('Max Value',0,20,10)


# country filter with pre selection

country_options = st.sidebar.multiselect('Countries', 
        ['Philippines', 'Brazil', 'Australia', 'United States of America',
       'Canada', 'Singapure', 'United Arab Emirates', 'India',
       'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa',
       'Sri Lanka', 'Turkey'], 
        default= ['Brazil','England','Qatar', 'South Africa', 'Canada','Australia'] ) 

# cuisines filter with pre selection
couisines_options = st.sidebar.multiselect('Cuisines',['Italian', 'European', 'Filipino', 'American', 'Korean', 'Pizza', 'Taiwanese', 'Japanese', 'Coffee', 'Chinese', 'Seafood',
       'Singaporean', 'Vietnamese', 'Latin American', 'Healthy Food',
       'Cafe', 'Fast Food', 'Brazilian', 'Argentine', 'Arabian', 'Bakery',
       'Tex-Mex', 'Bar Food', 'International', 'French', 'Steak',
       'German', 'Sushi', 'Grill', 'Peruvian', 'North Eastern',
       'Ice Cream', 'Burger', 'Mexican', 'Vegetarian', 'Contemporary',
       'Desserts', 'Juices', 'Beverages', 'Spanish', 'Thai', 'Indian',
       'Mineira', 'BBQ', 'Mongolian', 'Portuguese', 'Greek', 'Asian',
       'Author', 'Gourmet Fast Food', 'Lebanese', 'Modern Australian',
       'African', 'Coffee and Tea', 'Australian', 'Middle Eastern',
       'Malaysian', 'Tapas', 'New American', 'Pub Food', 'Southern',
       'Diner', 'Donuts', 'Southwestern', 'Sandwich', 'Irish',
       'Mediterranean', 'Cafe Food', 'Korean BBQ', 'Fusion', 'Canadian',
       'Breakfast', 'Cajun', 'New Mexican', 'Belgian', 'Cuban', 'Taco',
       'Caribbean', 'Polish', 'Deli', 'British', 'California', 'Others',
       'Eastern European', 'Creole', 'Ramen', 'Ukrainian', 'Hawaiian',
       'Patisserie', 'Yum Cha', 'Pacific Northwest', 'Tea', 'Moroccan',
       'Burmese', 'Dim Sum', 'Crepes', 'Fish and Chips', 'Russian',
       'Continental', 'South Indian', 'North Indian', 'Salad',
       'Finger Food', 'Mandi', 'Turkish', 'Kerala', 'Pakistani',
       'Biryani', 'Street Food', 'Nepalese', 'Goan', 'Iranian', 'Mughlai',
       'Rajasthani', 'Mithai', 'Maharashtrian', 'Gujarati', 'Rolls',
       'Momos', 'Parsi', 'Modern Indian', 'Andhra', 'Tibetan', 'Kebab',
       'Chettinad', 'Bengali', 'Assamese', 'Naga', 'Hyderabadi', 'Awadhi',
       'Afghan', 'Lucknowi', 'Charcoal Chicken', 'Mangalorean',
       'Egyptian', 'Malwani', 'Armenian', 'Roast Chicken', 'Indonesian',
       'Western', 'Dimsum', 'Sunda', 'Kiwi', 'Asian Fusion', 'Pan Asian',
       'Balti', 'Scottish', 'Cantonese', 'Sri Lankan', 'Khaleeji',
       'South African', 'Drinks Only', 'Durban', 'World Cuisine',
       'Izgara', 'Home-made', 'Giblets', 'Fresh Fish', 'Restaurant Cafe',
       'Kumpir', 'Döner', 'Turkish Pizza', 'Ottoman', 'Old Turkish Bars',
       'Kokoreç'], default= ['Home-made', 'BBQ','Italian','American','Brazilian', 'Japanese', 'Arabian'] )

linhas_selecionadas = df1['Country Name'].isin(country_options)
df1 = df1.loc[linhas_selecionadas, :]

# page title

st.header('Cuisines overview 🍽️')
st.write('##### Best restaurants rating')

# columns

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
	df1_aux = pd.DataFrame(df1.loc[:, ['Cuisines', 'Restaurant Name', 'Aggregate rating']])
	df1_aux2 = df1_aux.sort_values(by='Aggregate rating', ascending = False)
	organizado_por_nota = df1_aux2.sort_values('Aggregate rating', ascending=False)
	tipo_cozinha = df1_aux2.iloc[1,0]
	tipo_nome_resto = df1_aux2.iloc[1,1]
	nota_resto = df1_aux2.iloc[1,2]
	st.metric(label=f'{tipo_cozinha}: {tipo_nome_resto}', value=f'{nota_resto}/5.0')
		
with col2:
	df1_aux = pd.DataFrame(df1.loc[:, ['Cuisines', 'Restaurant Name', 'Aggregate rating']])
	df1_aux2 = df1_aux.sort_values(by='Aggregate rating', ascending = False)
	organizado_por_nota = df1_aux2.sort_values('Aggregate rating', ascending=False)
	tipo_cozinha = df1_aux2.iloc[2,0]
	tipo_nome_resto = df1_aux2.iloc[2,1]
	nota_resto = df1_aux2.iloc[2,2]
	st.metric(label=f'{tipo_cozinha}: {tipo_nome_resto}', value=f'{nota_resto}/5.0')

with col3:
	df1_aux = pd.DataFrame(df1.loc[:, ['Cuisines', 'Restaurant Name', 'Aggregate rating']])
	df1_aux2 = df1_aux.sort_values(by='Aggregate rating', ascending = False)
	organizado_por_nota = df1_aux2.sort_values('Aggregate rating', ascending=False)
	tipo_cozinha = df1_aux2.iloc[3,0]
	tipo_nome_resto = df1_aux2.iloc[3,1]
	nota_resto = df1_aux2.iloc[3,2]
	st.metric(label=f'{tipo_cozinha}: {tipo_nome_resto}', value=f'{nota_resto}/5.0')
	

with col4:
	df1_aux = pd.DataFrame(df1.loc[:, ['Cuisines', 'Restaurant Name', 'Aggregate rating']])
	df1_aux2 = df1_aux.sort_values(by='Aggregate rating', ascending = False)
	organizado_por_nota = df1_aux2.sort_values('Aggregate rating', ascending=False)
	tipo_cozinha = df1_aux2.iloc[4,0]
	tipo_nome_resto = df1_aux2.iloc[4,1]
	nota_resto = df1_aux2.iloc[4,2]
	st.metric(label=f'{tipo_cozinha}: {tipo_nome_resto}', value=f'{nota_resto}/5.0')
	
with col5:
	df1_aux = pd.DataFrame(df1.loc[:, ['Cuisines', 'Restaurant Name', 'Aggregate rating']])
	df1_aux2 = df1_aux.sort_values(by='Aggregate rating', ascending = False)
	organizado_por_nota = df1_aux2.sort_values('Aggregate rating', ascending=False)
	tipo_cozinha = df1_aux2.iloc[5,0]
	tipo_nome_resto = df1_aux2.iloc[5,1]
	nota_resto = df1_aux2.iloc[5,2]
	st.metric(label=f'{tipo_cozinha}: {tipo_nome_resto}', value=f'{nota_resto}/5.0')
	

# adjusting column ['Restaurant ID'] to str for stetic only.
df1['Restaurant ID'] = df1['Restaurant ID'].astype(str)

# selecting data to use
df_aux = df1.loc[:,['Restaurant ID', 'Restaurant Name', 'Country Name', 'City', 'Cuisines', 'Average Cost for two', 'Aggregate rating','Votes']].groupby(['Restaurant ID', 'Restaurant Name', 'Country Name', 'City', 'Cuisines', 'Average Cost for two', 'Aggregate rating','Votes']).mean().reset_index().sort_values('Aggregate rating', ascending = False)

linhas_visiveis = data_slider #ligando o slider ao dataframe para ser interativo

st.write('##### Details in dataframe')
# conecting dataframe to slider filter
st.dataframe(df_aux.head(linhas_visiveis), hide_index=True)

# selecting columns
col1,col2 = st.columns(2)
with col1:
# selecting data for chart 
	df1_aux = df1.loc[:,['Cuisines', 'Aggregate rating','lista']]
	restaurante_media_alta = df1_aux.loc[df1_aux['Aggregate rating']>4.0,:].groupby(['Cuisines']).mean().reset_index().sort_values('Aggregate rating', ascending=False)
	fig02 = px.bar(restaurante_media_alta[1:linhas_visiveis+1], 
				   x='Cuisines', 
				   y='Aggregate rating', 
				   labels= {'Cuisines': 'Registered cuisines','Aggregate rating': 'Average rates'},
				   title= "Top 10 best cuisines", text_auto=True)# creating bar chart
	st.plotly_chart(fig02, use_container_width = True)

with col2:
	df1_aux = df1.loc[:,['Cuisines', 'Aggregate rating','lista']]# selecting data for chart 
	restaurantes_pior_media = df1_aux.iloc[:,:].groupby(['Cuisines']).mean().sort_values('Aggregate rating', ascending=True).reset_index()
	fig02 = px.bar(restaurantes_pior_media[2:linhas_visiveis+2], 
				   x='Cuisines', 
				   y='Aggregate rating', 
				   labels= {'Cuisines': 'Registered cuisines','Aggregate rating': 'Avarage rating'} , 
				   title= "Top 10 worst cuisines", text_auto=True) # creating bar chart
	st.plotly_chart(fig02, use_container_width = True)