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