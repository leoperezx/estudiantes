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
    # Creo una sidebar para tomar una opción
    
    departamento_seleccionado = st.selectbox('Selecciona el departamento:',lista_departamentos)
    # creo un condicional para determinar que tan grande es la selección
    # df_filtrado = df_matriculas[df_matriculas['INSTITUCIÓN DE EDUCACIÓN SUPERIOR (IES)'] == departamento_seleccionado]
    # Título de la entrega de la información    
    st.subheader(f'Datos Filtrados para: {departamento_seleccionado}')
    
    df_departamento=fn.df_filtro_departamento(df_matriculas,departamento_seleccionado)
    # conteo de los registro de matrícula de acuerdo a la selección
    st.write(f'Número de registros: **{len(df_departamento)}**')
    # muestra la información flitrada
    # st.dataframe(df_filtrado,hide_index=True)

    matriculas_por_departamento = fn.matriculas_por_departamento(df_departamento)
    # print(matriculas_por_ies)
    
    st.dataframe(matriculas_por_departamento)
    # print(matriculas_por_ies[0].dtypes)
    sumatoria_por_IES = fn.top_10_IES_sumatoria(df_departamento)
    print(sumatoria_por_IES.sort_values(ascending=False).head(20))
    
    # tareas
    # - imprimir lista de IES en streamlit
    # - hacer graficas (torta o barras con porcentajes )
    # - separar info de posgrados 
    # - imprimir lista por áreas
    # - separar info por programas
    # - hacer graficas de los programas (torta o barras con porcentajes)

with tabs[1]:
     st.subheader('Limpieza de datos')
