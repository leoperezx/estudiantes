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

archivo_SNIES_2022 = 'data/prosessed/info_reducida_2022_limpia.csv'
archivo_OLE = 'data/prosessed/df_observador_laboral_pregrado.csv'
# # print(df.info())
# # print(df.columns)
df_matriculas = fn.cargar_datos(archivo_SNIES_2022)

st.title('Datos sobre el sistema educativo en Colombia - 2022')
st.markdown(''' 
            En el [Sistema Nacional de Información de la Educación Superior - SNIES](https://snies.mineducacion.gov.co/portal/ESTADISTICAS/Bases-consolidadas/) se encuentran diferentes bases de datos sobre los estudiantes inscritos, admitidos y matriculados en las instituciones de educación superior en Colombia. 
            
            Estas bases de datos son la materia prima de este "tablero" que invita a estudiantes, maestros, padres de familia o acudientes a ver de una forma mas comoda los datos registrados por el SNIES. 
            
            Developed by | :blue-background[@leoperez.x]
            ''')

st.divider()

st.header('Bienvenido al panel de datos')
st.text(f'El conjunto de datos tiene {len(df_matriculas)} registros de matrículas, pero este panel filtra por departamento y realiza graficas sobre el número de matrículas de estudiantes de prosgrado y pregrado organizandolos de mayor a menor mostrando las instituciones educativas, las áreas de conocimiento y los programas con mayor número de matrículas en el año 2022.')
# st.dataframe(df_matriculas.head())

tab1, tab2 = st.tabs(['Info por departamento','Observatorio laboral'])
# tabs = st.tabs(['Info por departamento','Observatorio laboral'])

st.sidebar.header("Controles", text_alignment="center")
    
with tab1:
    st.subheader('Información por departamento')
    # Creo una lista de las universidades
    lista_de_departamentos = df_matriculas['DEPARTAMENTO DE OFERTA DEL PROGRAMA'].unique()
    # contateno la lista de universidades con la "Todas".
    lista_departamentos = list(lista_de_departamentos)
    # Creo un selectbox para tomar una opción
    st.sidebar.subheader("Info por departamento")
    departamento_seleccionado = st.sidebar.selectbox('Selecciona el departamento:',lista_departamentos)
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


    
with tab2:
    st.subheader('Limpieza de datos')
    st.markdown(''' 
                El presente código trabaja con una base de datos que contiene información sobre el número de graduados de diferentes carreras. La base de datos original se puede descargar del [_Observatorio Laboral para la Educación - OLE_](https://ole.mineducacion.gov.co/portal/secciones/Estudios-y-documentos/Tablas-de-salida-y-Bases-de-Datos/#data=%7B%22filter%22:%2268247%22,%22page%22:1%7D).
                
                Las funciones del Observatorio Laboral para la Educación y en general de otras entidades que están relacionadas con los estudios de seguimiento a graduados, mercado laboral y capital humano calificado son recopilar y analizar información relevante al mercado laboral de los egresados de pregrado y posgrado.

                Dentro de la pagina oficial se pueden filtrar consultas por el año de publicación, en este caso se filtro por el año mas reciente disponible que para la fecha de la realización de este algoritmo fue el 2023.
                ''')
    
    df_egresados = fn.cargar_datos(archivo_OLE)
    
    st.sidebar.divider()
    st.sidebar.subheader("Observatorio laboral")
    anho_seleccionado = st.sidebar.selectbox("📅 Selecciona el Año de Grado:", fn.lista_anhos_disponebles(df_egresados))
    
    df_filtrado_anho = fn.df_filtrado_anhos(df_egresados,anho_seleccionado)
    
    df_agrupado_prog_sex = fn.df_filtrado_agrupado_programa_y_sexo(df_filtrado_anho)
    
    df_top_20 = fn.top_20_programas(df_agrupado_prog_sex)
    
    # st.dataframe(df_top_20)
    
    grafica_top_20 = fn.generando_grafica_top_20(df_top_20,anho_seleccionado)
    
    st.plotly_chart(grafica_top_20)
