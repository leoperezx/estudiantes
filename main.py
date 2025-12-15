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

# tabs = st.tabs(['Datos generales','Limpieza de datos'])
# with tabs[0]:
#     st.subheader('Datos Generales')
#     # Creo una lista de las universidades
#     lista_de_universidades = df_matriculas['INSTITUCIÓN DE EDUCACIÓN SUPERIOR (IES)'].unique()
#     # contateno la lista de universidades con la "Todas".
#     lista_universidades_con_todas = ['Todas'] + list(lista_de_universidades)
#     # Creo una sidebar para tomar una opción
#     universidad_seleccionada = st.sidebar.selectbox('Selecciona la Institución:',lista_universidades_con_todas)
#     # creo un condicional para determinar que tan grande es la selección
#     if universidad_seleccionada == 'Todas':
#         df_filtrado = df_matriculas
#     else:
#         # Comando clave de Pandas para filtrar:
#         df_filtrado = df_matriculas[df_matriculas['INSTITUCIÓN DE EDUCACIÓN SUPERIOR (IES)'] == universidad_seleccionada]
#     # Título de la entrega de la información    
#     st.subheader(f'Datos Filtrados para: {universidad_seleccionada}')
#     # conteo de los registro de matrícula de acuerdo a la selección
#     st.write(f'Número de registros: **{len(df_filtrado)}**')
#     # muestra la información flitrada
#     st.dataframe(df_filtrado,hide_index=True)

#     matriculas_por_ies = fn.matriculas_por_ies(df_matriculas)
#     # print(matriculas_por_ies)
    
#     st.dataframe(matriculas_por_ies)
#     # print(matriculas_por_ies[0].dtypes)
#     # sumatoria_por_seleccion_de_ies = matriculas_por_ies[1].sum()
#     # st.text(f'total de matriculados es: {sumatoria_por_seleccion_de_ies}')

# with tabs[1]:
#      st.subheader('Limpieza de datos')
