# Estudio y análisis de las matriculas de Entidades de Educación superior

Colombia 2022

## Resumen

A continuación se presenta un desarrollo de análisis de datos como tema de estudio y práctica autodidacta. No soy ningun experto y busco realizar un buen proyecto como medio para aprender temas de arquitectura, estructura y programación con python y streamlit. Por otra parte, la intención de este proyecto es realizar un estudio sobre la tendencia de los estudiantes de bachillerato a la hora de escoger carrera en las universidades.

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

¡Con estos comandos, puedes empezar a desarrollar tu proyecto de forma aislada y colaborativa usando ramas localmente!.

> Hecho por [**@leoperez.x**](leoperez.x@gmail.com) | 2025
