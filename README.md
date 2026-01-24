# Estudio y análisis de las matriculas de Entidades de Educación superior

Colombia 2022

## Resumen

A continuación se presenta un desarrollo de análisis de datos como tema de estudio y práctica autodidacta. El presente proyecto se encuetra en desarrollo y en consturcción. No soy ningun experto, seguramente tendra errores y mejores procedimientos. No busco realizar un buen proyecto perfecto a la primera pero, si busco aprender temas de arquitectura, estructura de directorios, manejo de github, programación con python y streamlit. Cualquier sujerencia es bien recibida. Por otra parte, la intención de este proyecto es realizar un estudio sobre la tendencia de los estudiantes de bachillerato a la hora de escoger carrera en las universidades. Soy maestro y me gustaría poder entregarle a mis estudiantes de bachillerato un herramienta un análisis a la hora de escoger carrera.

## Línea de desarrollo

Planteo una línea de trabajo o desarrollo en donde plasmo mi ruta de trabajo. Además organizo mis directorios en donde voy añadiendo los diferentes algoritmos. Mi flujo de trabajo es desarrollar diferentes bases en la producción. La primer face es hacer _pruebas_ utilizando los archivos de _Jupyter_. Todas estas pruebas se alojan en el directorio _notebook_ y son el insumo de los _archivos fuente_ en el directorio _src_. La segunsa fase son los archivos en el directorio _src_, los cuales están organizados de una mejor forma o incluso con una _refactorización_ de los códigos del _Jupyter_. En esta face espero organizar los _archivos fuente_ que voy a ir ejecutando y retornando archivos csv en el directorio _data/prosessed_ que su vez serán utilizados en nuevas _pruebas_ y _archivos fuente_. Por último la fase tres es el desarrollo de un _dashboard_ con "Streamlit" y para hacerlo me voy a apoyar en muchos de los _archivos fuente_ usandolos como "modulos" invocando las funciones. 

## 📊 Análisis General de Demanda

Estas ideas te ayudarán a entender la distribución básica de la matrícula.

* **Top IES por Matrícula Total:** Identifica las **10 o 20 Instituciones de Educación Superior (IES)** con el mayor número de estudiantes matriculados. Esto te da una visión de las instituciones más grandes y demandadas a nivel nacional.
* **Distribución por Nivel Académico:** Analiza cómo se distribuye la matrícula entre los diferentes **'NIVELES ACADÉMICOS'** (e.g., pregrado, posgrado, técnico profesional, tecnológico). Esto revela dónde se concentra la mayor demanda educativa.
* **Distribución Geográfica:** Utiliza las columnas **'DEPARTAMENTO DE OFERTA DEL PROGRAMA'** y **'MUNICIPIO DE OFERTA DEL PROGRAMA'** para identificar las regiones (departamentos y ciudades) con la mayor concentración de estudiantes matriculados.

---

## 🔬 Análisis Específico de Programas y Áreas

Estas ideas se centran en los intereses académicos de los estudiantes.

* **Programas más Demandados:** Genera un *ranking* de los **'PROGRAMAS ACADÉMICOS'** individuales con mayor matrícula a nivel nacional o por departamento. ¿Cuáles son las carreras más populares?
* **Demanda por Área de Conocimiento:** Agrupa la matrícula por **'ÁREA DE CONOCIMIENTO'** (e.g., Ingeniería, Ciencias de la Salud, Ciencias Sociales). Esto te permite ver las grandes tendencias de demanda en el mercado laboral y académico.
* **Áreas de Crecimiento/Disminución (si tienes datos de semestres):** Si tu columna **'SEMESTRE'** permite diferenciar el primer y segundo semestre de 2022, puedes comparar la matrícula para ver qué áreas o programas tuvieron un cambio en la demanda en el transcurso del año.

---

## 👩‍🔬 Análisis Demográfico y de Equidad

Esta perspectiva te permite entender a quién está sirviendo el sistema.

* **Demanda por Sexo:** Compara la distribución de la matrícula según la columna **'SEXO'** (Hombres vs. Mujeres) a nivel total, por IES, o—lo que es más interesante—por **'ÁREA DE CONOCIMIENTO'** o **'PROGRAMA ACADÉMICO'**. Por ejemplo, ¿qué programas tienen una mayor desbalance de género?
* **Concentración en IES específicas:** Para programas o áreas muy demandadas, analiza la concentración; es decir, ¿cuántas IES cubren el 80% de la matrícula total de ese programa? Esto indica si la demanda está dispersa o si se concentra en unas pocas instituciones líderes.

---

## 🎯 Ideas Avanzadas para Visualización

**Gráfico de Burbujas:** Crea un gráfico donde:

* El **eje X** sea la Matrícula Total por IES.
* El **eje Y** sea el Número de Programas Ofrecidos por IES (puedes calcular esto contando programas únicos por IES).
* El **tamaño de la burbuja** represente la Matrícula promedio por Programa.
* Esto te ayudará a diferenciar entre IES grandes con muchos programas ("generalistas") y IES especializadas con alta demanda en pocos programas ("nichos").
* **Mapa de Calor:** Utiliza un mapa de calor para cruzar las **'ÁREAS DE CONOCIMIENTO'** (filas) con los **'DEPARTAMENTOS'** (columnas). Los colores más intensos señalarán las áreas de mayor demanda en cada región.

## ESQUEMA BÁSICO DE CARPETAS (Arquitectura)

```text
mi_proyecto_analisis/
├── data/
│   ├── raw/           # Datos originales (NUNCA se modifican)
│   ├── processed/     # Datos limpios/transformados listos para el análisis
├── notebooks/         # Jupyter Notebooks para exploración y prototipado
├── src/               # Código fuente de Python (scripts/módulos)
│   ├── data_loading.py    # Funciones para cargar/limpiar los datos
│   ├── features.py        # Funciones para crear nuevas características
│   ├── analysis.py        # Funciones de análisis estadístico/modelado
│   ├── visualization.py   # Funciones de trazado (gráficas)
├── app/
│   └── main_app.py    # Tu aplicación Streamlit (interfaz de usuario)
├── .gitignore         # Archivos que Git debe ignorar (ej. 'env/', '__pycache__/')
├── requirements.txt   # Dependencias de Python (pandas, streamlit, etc.)
└── README.md          # Documentación del proyecto
```

## Trabajando con GIT - Comandos básicos

Para iniciar Git y trabajar con ramas localmente, primero inicializa un repositorio con git init, luego crea y cambia a una rama con `git checkout -b <nombre-rama>`, haz tus cambios, añádelos con `git add .` y confírmalos con `git commit -m "Mensaje"`, usando `git branch` para listar ramas y `git merge` para unirlas después, comandos clave para el flujo de trabajo de ramas en tu máquina.

### Pasos para empezar con Git localmente y ramas

#### Inicializar un repositorio (si es un proyecto nuevo)

* Navega a la carpeta de tu proyecto en la terminal: `cd /ruta/a/tu/proyecto.
* Inicializa Git: `git init` (esto crea la carpeta .git).

#### Crear y cambiar a una nueva rama

* Usa `git branch <nombre-de-tu-rama>` para crearla.
* Para crearla y cambiarte a ella en un solo paso, usa: `git checkout -b nueva-funcionalidad`.

#### Trabajar en tu rama

* Haz cambios en tus archivos.
* Prepara los cambios: `git add .` (para todos los archivos).
* Confirma los cambios: `git commit -m "Descripción de los cambios"`.

#### Gestionar ramas

* Ver todas las ramas locales: `git branch`.
* Cambiar a otra rama: `git checkout nombre-de-otra-rama`.
* Fusionar otra rama en tu rama actual: `git merge nombre-de-la-rama-a-fusionar`.

#### Flujo común (después de clonar un repo remoto)

* `git clone <URL-del-repositorio>` para obtenerlo.
* `git checkout -b mi-nueva-rama`.
* Trabaja, añade y commitea.
* Publica la rama remota (¡si tienes un repo remoto!): `git push -u origin mi-nueva-rama`.

## Trabajando con STREAMLIT - Comandos básicos

Streamlit es una biblioteca de Python para crear aplicaciones web de datos rápidamente. Los comandos básicos incluyen `st.write()` para texto/datos, `st.title()` para títulos, y widgets interactivos como `st.button()`, `st.slider()`, y `st.text_input()`. Se ejecutan con `streamlit run app.py`. 

### Aquí tienes los comandos fundamentales organizados por categoría:

#### 1. Configuración y Ejecución

- `import streamlit as st`: Importar la biblioteca.
- `$ streamlit run app.py`: Ejecutar la aplicación en la terminal.
- `st.set_page_config(page_title="Título", layout="wide")`: Configurar el título de la pestaña del navegador y el diseño. 

#### 2. Visualización de Texto y Datos

- `st.title("Título")`: Título principal.
- `st.header("Encabezado")`: Encabezado de sección.
- `st.subheader("Subencabezado")`: Subencabezado.
- `st.write("Texto o variables")`: Escribir texto, datos, gráficos, etc..
- `st.markdown("Texto en *Markdown*")`: Renderizar texto con formato Markdown.
- `st.dataframe(df)`: Mostrar un DataFrame de Pandas interactivo.
- `st.table(df)`: Mostrar una tabla estática.
- `st.json({"key": "value"})`: Mostrar objetos JSON. 

#### 3. Widgets Interactivos (Entrada de datos)

- `st.button("Hacer clic")`: Botón interactivo.
- `st.checkbox("Opción")`: Casilla de verificación.
- `st.radio("Elegir", ["A", "B"])`: Botones de opción.
- `st.selectbox("Seleccionar", ["A", "B"])`: Menú desplegable.
- `st.text_input("Nombre")`: Campo de entrada de texto.
- `st.number_input("Edad", min_value=0, max_value=100)`: Entrada numérica.
- `st.slider("Seleccionar valor", 0, 100)`: Deslizador.
- `st.file_uploader("Subir archivo")`: Componente para cargar archivos. 

#### 4. Visualización de Gráficos

- `st.line_chart(datos)`: Gráfico de líneas.
- `st.area_chart(datos)`: Gráfico de áreas.
- `st.bar_chart(datos)`: Gráfico de barras. 

#### 5. Diseño y Organización (Layouts)

- `st.sidebar`: Añadir elementos a la barra lateral (ej: `st.sidebar.selectbox(...)`).
- `col1, col2 = st.columns(2)`: Crear columnas.
- `with st.expander("Ver más"):`: Crear un contenedor expandible. 

#### 6. Mensajes de Estado

- `st.success("Operación exitosa")`: Mensaje verde.
- `st.info("Información")`: Mensaje azul.
- `st.warning("Advertencia")`: Mensaje amarillo.
- `st.error("Error")`: Mensaje rojo.
- `st.balloons()`: Mostrar animación de globos.
- `st.snow()`: Mostrar animación de nieve. 

Los "comandos mágicos" permiten escribir directamente texto o variables sin st.write().

¡Con estos comandos, puedes empezar a desarrollar tu proyecto de forma aislada y colaborativa usando ramas localmente!.

> Hecho por [**@leoperez.x**](leoperez.x@gmail.com) | 2026
