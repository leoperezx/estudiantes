# El presente algoritmo pretende ser un estudio y presentacion
# de los estudiantes matriculados en el valle del cauca en el 
# año 2022. La información se extrae del Sistema Nacional de 
# Información de la Educación Superior - SNIES.
# --------------------------------------------------------------------------
# https://snies.mineducacion.gov.co/portal/ESTADISTICAS/Bases-consolidadas/
# --------------------------------------------------------------------------

import src.funciones as fn # La ruta relativa cambia los "/" por "."  
import streamlit as st
st.set_page_config(layout="wide")

archivo = 'data/prosessed/info_reducida_2022_limpia.csv'

# # print(df.info())
# # print(df.columns)
df_matriculas = fn.cargar_datos(archivo)

st.title('Análisis de matriculas universitarias - 2022')
st.header('Bienvenido al panel de datos')
st.text(f'El conjunto de datos tiene {len(df_matriculas)} registros de matrículas pero, sólo se muestran las 5 primeras filas. ')
st.dataframe(df_matriculas.head())

tabs = st.tabs(['Info por departamento','Limpieza de datos'])
with tabs[0]:
    st.subheader('Info por departamento')
    # Creo una lista de las universidades
    lista_de_departamentos = df_matriculas['DEPARTAMENTO DE OFERTA DEL PROGRAMA'].unique()
    # contateno la lista de universidades con la "Todas".
    lista_departamentos = list(lista_de_departamentos)
    # Creo un selectbox para tomar una opción
    departamento_seleccionado = st.selectbox('Selecciona el departamento:',lista_departamentos)
    # Creo un título con el departamento seleccionado   
    st.subheader(f'Datos Filtrados para: {departamento_seleccionado}')
    # Creo el dataframe del departamento seleccionado
    df_departamento=fn.df_filtro_departamento(df_matriculas,departamento_seleccionado)
    # conteo de los registro de matrícula de acuerdo a la selección
    st.write(f'Número de registros: **{len(df_departamento)}**')
    
    sumatoria_por_IES = fn.top_10_IES_sumatoria(df_departamento).sort_values(ascending=False).head(20)
    # la respuesta es una Serie por lo que hay que separar los index de los valores y convertirlos a df.
    data_sumatoria_por_IES = fn.convertir_a_df(sumatoria_por_IES)
    
    # Organizando arquitectura de streamlit 
    # Crear dos columnas: la primera ocupa 60% del espacio y la segunda 40%
    col_ancho1, col_ancho2 = st.columns([0.6, 0.4])
    
    with col_ancho1:
        # Imprime dataframe
        st.dataframe(data_sumatoria_por_IES)
      
    with col_ancho2:
        # Crea un gráfico de barras
        st.bar_chart(data_sumatoria_por_IES.set_index('Index'), x_label="Número de matrículas", y_label="IES", horizontal=True, sort="-Valores") 
    
    # - separar info de posgrados 
    # - imprimir lista por áreas
    # - separar info por programas
    # - hacer graficas de los programas (torta o barras con porcentajes)

with tabs[1]:
     st.subheader('Limpieza de datos')
