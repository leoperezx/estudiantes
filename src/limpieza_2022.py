import pandas as pd
# Cargando la información
df = pd.read_excel("../data/raw/estudiantes_matriculados-2022_recurso.xlsx", sheet_name=["Matriculados E.S. 2022"], header=8)
# Creo un data frame con la información dentro del diccionario.
df_data = pd.DataFrame(df['Matriculados E.S. 2022']) 
# Selecciono solo los atributos necesario para este primer análisis.
df_info_limitado_2022 = df_data[['INSTITUCIÓN DE EDUCACIÓN SUPERIOR (IES)',
                      'PROGRAMA ACADÉMICO',
                      'NIVEL ACADÉMICO',
                      'ÁREA DE CONOCIMIENTO',
                      'DEPARTAMENTO DE OFERTA DEL PROGRAMA',
                      'MUNICIPIO DE OFERTA DEL PROGRAMA',
                      'SEXO',
                      'SEMESTRE',
                      'MATRICULADOS']]
# Elimino las líneas duplicadas de la información reducida con solo los atributos esensiales.
df_info_limitado_2022_sin_duplicados = df_info_limitado_2022.drop_duplicates()
# Imprimo en pantalla los traibutos del dataframe reducido y lipiado del año 2022. 
print(f"\n Lista de columnas y tipos de datos: \n{df_info_limitado_2022_sin_duplicados.dtypes}")
# guardo como archivo de texto plano [.csv]
df_info_limitado_2022_sin_duplicados.to_csv('../data/prosessed/info_reducida_2022_limpia.csv', index=False)