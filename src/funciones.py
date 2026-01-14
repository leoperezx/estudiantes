# Algoritmo complento del archivo posgrados.py
import pandas as pd
import streamlit as st

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

def matriculas_por_departamento(archivo):
    return archivo.groupby('DEPARTAMENTO DE OFERTA DEL PROGRAMA')['MATRICULADOS'].sum().reset_index()    

def df_filtro_departamento(df,departamento):
    return df[df['DEPARTAMENTO DE OFERTA DEL PROGRAMA'].isin([departamento])] 

def top_10_IES_sumatoria(df):
    return df.groupby('INSTITUCIÓN DE EDUCACIÓN SUPERIOR (IES)')['MATRICULADOS'].sum()   
    