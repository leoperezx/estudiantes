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
    st.subheader('Información por departamento')
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
    
    # Organizando arquitectura de streamlit 
    # Crear dos columnas: la primera ocupa 60% del espacio y la segunda 40%
    
    
    row1=st.container(border=True)
    row2=st.container(border=True)
    row3=st.container()
    col1, col2 = row1.columns([0.5, 0.5])
    col3, col4 = row2.columns([0.5, 0.5])
    
    with col1:
        sumatoria_por_IES = fn.top_10_IES_sumatoria(df_departamento).sort_values(ascending=False).head(10)
        # la respuesta es una Serie por lo que hay que separar los index de los valores y convertirlos a df.
        data_sumatoria_por_IES = fn.convertir_a_df(sumatoria_por_IES)
        st.subheader("Gráfica de matrículas de Posgrado y pregrado", text_alignment='center')
        grafica=fn.generando_grafica(data_sumatoria_por_IES,"Matrículas","IES")
        st.plotly_chart(grafica)
        
    df_posgrados = fn.df_filtro_posgrados(df_departamento,nivel='POSGRADO')  # solo se unas df_posgrados una vez
    
    with col2:
        sumatoria_por_posgrados = fn.top_10_IES_sumatoria(df_posgrados).sort_values(ascending=False).head(10)
        # la respuesta es una Serie por lo que hay que separar los index de los valores y convertirlos a df.
        data_sumatoria_por_posgrados = fn.convertir_a_df(sumatoria_por_posgrados)
        st.subheader("Gráfica de matrículas de Posgrado", text_alignment='center')
        grafica=fn.generando_grafica(data_sumatoria_por_posgrados,"Matrícula","IES")
        st.plotly_chart(grafica)
        
       
    with col3:
        sumatoria_por_Area_de_conocimiento = fn.Area_de_conocimiento_sumatoria(df_departamento).sort_values(ascending=False)
        data_sumatoria_por_areas_de_conocimiento = fn.convertir_a_df(sumatoria_por_Area_de_conocimiento)
        st.subheader("Gráfica de matrículas por áreas de conocimiento", text_alignment='center')
        grafica=fn.generando_grafica(data_sumatoria_por_areas_de_conocimiento,"Matrícula","Áreas de conocimiento")
        st.plotly_chart(grafica)
      
    with col4:
        # Imprime dataframe
        st.write("Gráfica por nombre del programa")
        sumatoria_por_programa_academico = fn.programa_academico_sumatoria(df_departamento).sort_values(ascending=False).head(10)
        data_sumatoria_por_programa_academico = fn.convertir_a_df(sumatoria_por_programa_academico)
        st.subheader("Gráfica de matrículas por programa académico", text_alignment='center')
        grafica=fn.generando_grafica(data_sumatoria_por_programa_academico,"Matrícula","Programa académico")
        st.plotly_chart(grafica)
    
    # - imprimir lista por áreas
    # - separar info por programas
    # - hacer graficas de los programas (torta o barras con porcentajes)
    
    # - 

with tabs[1]:
     st.subheader('Limpieza de datos')
