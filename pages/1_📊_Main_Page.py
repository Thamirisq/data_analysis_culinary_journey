#library used
import pandas as pd
import numpy as np

import plotly.express as px
import matplotlib as mp
import folium
from   folium.plugins import MarkerCluster
from   io import BytesIO
from   xlsxwriter import Workbook

import streamlit as st
from streamlit_folium import folium_static
from PIL import Image

# Page Name
st.set_page_config(page_title="Main Page",page_icon="📊")

# file imported
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

# ============================== menu principal ===============================================================
image_path = 'logo.png'
image = Image.open(image_path) 

# Page title
st.write('# Culinary Journey 📊')
st.write('### Best place to find your new favorite restaurant!!')

# sidebar logo
image_path = 'logo.png'
image = Image.open(image_path) 

#centralizando logo e nome
col1, col2 = st.sidebar.columns([1, 2])
with col1:
    st.image("logo.png", width=70)
with col2:
	st.write("# Culinary Journey")
st.sidebar.write('### Filters options')

# columns with only one information requested.

rest_unic = df1['Restaurant ID'].nunique()
rest_unic_formatado = f'{rest_unic:,}'.replace(",", ".") #ajustando o formato do número com ponto. 
country_unic = df1['Country Code'].nunique()
city_unic = df1['City'].nunique()
aval_total = df1['Votes'].sum()
aval_total_formatado = f'{aval_total:,}'.replace(",", ".") #ajustando o formato do número com ponto. 
cuisines_types = df1.loc[:,'Cuisines'].nunique()

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Restaurants",rest_unic_formatado)
col2.metric('Countries',country_unic)
col3.metric('Cities',city_unic)
col4.metric('Total ratings',aval_total_formatado)
col5.metric('Cuisines type',cuisines_types) 

# filters in sidebar with pre selection.
country_options = st.sidebar.multiselect('Countries', ['Philippines', 'Brazil', 'Australia', 'United States of America','Canada', 'Singapure', 'United Arab Emirates', 'India','Indonesia', 'New Zeland',            'England', 'Qatar', 'South Africa','Sri Lanka', 'Turkey'], default= ['Australia', 'Brazil', 'Canada','England', 'Qatar', 'South Africa'] )

linhas_selecionadas = df1['Country Name'].isin(country_options)
df1 = df1.loc[linhas_selecionadas, :]

st.write('###### Explore below map using the zoom or clicking in the circles or pointers.')
#  map data
df1_aux = df1.loc[:, ['Latitude', 'Longitude', 'City', 'Restaurant Name','Cuisines','Currency','Average Cost for two', 'Aggregate rating']]  .groupby(['Latitude', 'Longitude', 'City', 'Restaurant Name','Cuisines','Currency','Average Cost for two', 'Aggregate rating']).median().reset_index()

#  adjusting columns from 'int' em 'str' to popup concatenate.

df1_aux ['Average Cost for two'] = df1_aux['Average Cost for two'].astype(str)
df1_aux ['Aggregate rating'] = df1_aux['Aggregate rating'].astype(str)


#  creating a map
mapa = folium.Map()

#  creating the union of numbers on the map, called cluster.

marker_cluster = MarkerCluster().add_to(mapa)

#  creating mark and add to cluster.

for index, location_info in df1_aux.iterrows():
	folium.Marker([location_info['Latitude'],location_info['Longitude']], 
				  popup=
				    '<b><h5>' + df1_aux.iloc[index]['Restaurant Name'] + '</b> </h4>' 
				  + '<p>Price for two:&nbsp' + df1_aux.iloc[index]['Currency'] + df1_aux.iloc[index]['Average Cost for two'] 
				  + '<p>Type:&nbsp' + df1_aux.iloc[index]['Cuisines'] 
				  + '<p>Aggregate Rating:&nbsp' + df1_aux.iloc[index]['Aggregate rating'], width=400
				 ).add_to(marker_cluster)

# map dimensions 
folium_static(mapa, width=800, height=400)


# changing file to excel format
excel_buffer = BytesIO()
with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
	df1.to_excel(writer, index=False)
excel_data = excel_buffer.getvalue()

# making download button.
st.sidebar.download_button(
		label="Download Excel",
		data=excel_data,
		file_name='data.xlsx',
		key="excel_key",
		mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
	)