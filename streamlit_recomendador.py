
import streamlit as st
import pandas as pd

# Cargar la tabla con los datos
data = pd.read_excel('AYUDAVENTAS.xlsx')

st.title('Recomendación de Adhesivo Cemix')

# Paso 1: Selección del tipo de revestimiento
revestimiento = st.selectbox('Selecciona el tipo de revestimiento', data['REVESTIMIENTO'].unique())

# Filtrar las opciones por revestimiento seleccionado
filtered_data = data[data['REVESTIMIENTO'] == revestimiento]

# Paso 2: Selección del formato
formato = st.selectbox('Selecciona el formato del revestimiento', filtered_data['FORMATO'].unique())

# Filtrar por formato
filtered_data = filtered_data[filtered_data['FORMATO'] == formato]

# Paso 3: Selección del sustrato
sustrato = st.selectbox('Selecciona el sustrato', filtered_data['SUSTRATO'].unique())

# Filtrar por sustrato
filtered_data = filtered_data[filtered_data['SUSTRATO'] == sustrato]

# Paso 4: Selección de la superficie
superficie = st.selectbox('Selecciona la superficie', filtered_data['SUPERFICIE'].unique())

# Filtrar por superficie
filtered_data = filtered_data[filtered_data['SUPERFICIE'] == superficie]

# Paso 5: Selección del ambiente
ambiente = st.selectbox('Selecciona el ambiente', filtered_data['AMBIENTE'].unique())

# Filtrar por ambiente
filtered_data = filtered_data[filtered_data['AMBIENTE'] == ambiente]

# Paso 6: Selección de la incidencia climática
incidencia_climatica = st.selectbox('Selecciona la incidencia climática', filtered_data['INCIDENCIA CLIMATICA'].unique())

# Filtrar por incidencia climática
filtered_data = filtered_data[filtered_data['INCIDENCIA CLIMATICA'] == incidencia_climatica]

# Paso 7: Selección del uso
uso = st.selectbox('Selecciona el uso', filtered_data['USO'].unique())

# Filtrar por uso
filtered_data = filtered_data[filtered_data['USO'] == uso]

# Resultado final: mostrar la recomendación de adhesivo
if not filtered_data.empty:
    recomendacion = filtered_data['RECOMENDACION'].values[0]
    st.success(f'La recomendación de adhesivo es: {recomendacion}')
else:
    st.error('No se encontró una recomendación para esta combinación.')

