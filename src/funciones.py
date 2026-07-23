# Algoritmo complento del archivo posgrados.py
import pandas as pd
import streamlit as st
import plotly.express as px

def cargar_db (archivo):
    '''
    Entrada: 'archivo.vsc'.
    Salida: database en pandas.
    
    Objetivo: convierte un archivo csv en una base de datos en pandas.
    '''
    df = pd.read_csv(archivo)
    return df

@st.cache_data
def cargar_datos(archivo):
    # Asegúrate de usar la ruta correcta a tu archivo
    return pd.read_csv(archivo)

def df_filtro_departamento(df,departamento):
    return df[df['DEPARTAMENTO DE OFERTA DEL PROGRAMA'].isin([departamento])] 

def top_10_IES_sumatoria(df):
    return df.groupby('INSTITUCIÓN DE EDUCACIÓN SUPERIOR (IES)')['MATRICULADOS'].sum()   

def Area_de_conocimiento_sumatoria(df):
    return df.groupby('ÁREA DE CONOCIMIENTO')['MATRICULADOS'].sum()   

def programa_academico_sumatoria(df):
    return df.groupby('PROGRAMA ACADÉMICO')['MATRICULADOS'].sum()  

def convertir_a_df(df):
    valores_df = df.values
    index_df = df.index
    datos = {'Index': index_df, 'Valores': valores_df}
    return pd.DataFrame(datos)

def df_filtro_posgrados(df,nivel):
    return df[df['NIVEL ACADÉMICO'].isin([nivel])] 

def generando_grafica(df,x_label,y_label):
    df_invertido = df.iloc[::-1]
    fig = px.bar(df_invertido,x="Valores",y="Index",orientation='h',labels={"Valores": x_label, "Index":y_label})
    fig.update_layout(
        margin=dict(l=50, r=20, t=20, b=20),
        yaxis=dict(automargin=True)
    )
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
    return fig

# funciones para la sección del observador laboral para la educacion - OLE

def lista_anhos_disponebles(df):
    return sorted(df['AÑO DE GRADO'].unique(), reverse=True)

def df_filtrado_anhos(df, anho_seleccionado):
    return df[df['AÑO DE GRADO'] == anho_seleccionado]

def df_filtrado_agrupado_programa_y_sexo(df):
    return df.groupby(['PROGRAMA ACADÉMICO', 'SEXO'], as_index=False)['GRADUADOS'].sum()

def top_20_programas(df):
    top_programas = (
        df.groupby('PROGRAMA ACADÉMICO')['GRADUADOS']
        .sum()
        .nlargest(20)
        .index
    )
    return df[df['PROGRAMA ACADÉMICO'].isin(top_programas)]

def generando_grafica_top_20(df,anho_seleccionado):
    fig = px.bar(
        df,
        x='GRADUADOS',                # Ahora el número va en el eje X
        y='PROGRAMA ACADÉMICO',       # El nombre del programa va en el eje Y
        color='SEXO',
        title=f'Top 20 Programas Académicos con Mayor Número de Graduados con empleo en {anho_seleccionado} en Colombia',
        labels={'GRADUADOS': 'Total Graduados', 'PROGRAMA ACADÉMICO': 'Programa Académico'},
        barmode='group', 
        color_discrete_map={'FEMENINO': '#e066ff', 'MASCULINO': '#1f77b4'},
        orientation='h'               # Forzar orientación horizontal
    )
    fig.update_layout(
        height=700,                   # Más altura para que se lean bien los nombres
        yaxis={'categoryorder': 'total ascending'}, # Muestra el programa con más graduados arriba del todo
        margin=dict(l=200)            # Margen izquierdo extra para que no se corten los nombres largos
    )
    return fig