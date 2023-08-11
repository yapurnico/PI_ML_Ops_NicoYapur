################# Proyecto ML_OPS Henry-Bootcamp Nicolas Yapur ############################

# Sistema de Recomendación de Películas

"Dado dos archivos CSV que contienen información sobre películas, el propósito de este proyecto es crear una API que ofrezca seis funciones que proporcionen información relevante sobre los datos en forma de 6 funciones. Además, el proyecto incluye un Sistema de Recomendación de Películas basado en Machine Learning. El resultado de este modelo es una función que toma el nombre de una película como entrada y devuelve una lista de las cinco películas más similares a la ingresada."

## Índice

- Introducción
- ETL
- Desarrollo de la API
- EDA (Análisis Exploratorio de Datos)
- Aprendizaje Automático (Machine Learning)
- API y Video
- Archivos Adicionales

## Introducción

"Este proyecto es parte del Bootcamp de Ciencia de Datos de Henry (PI_ML_OPS). Sirve como el primero de tres proyectos requeridos para graduarse del Bootcamp y se divide en cinco pasos principales. El objetivo principal de este proyecto es transformar con éxito archivos de datos sin procesar en información relevante presentada en forma de seis preguntas y un sistema de recomendación.

El entregable del proyecto es una API completamente funcional construida utilizando FastAPI y desplegada en Render. A lo largo de este proyecto, aplicamos los conocimientos adquiridos durante el bootcamp en las áreas de Ingeniería de Datos y Ciencia de Datos para crear un proyecto similar a un caso real."

## ETL

La Extracción, Transformación y Carga (ETL) consistió en realizar los siguientes pasos:

- Creé el archivo 'ETL_movies_main.ipynb'. En este archivo, cargué el archivo CSV llamado 'movies_dataset.csv', que fue el primer archivo fuente, y realicé seis transformaciones principales, que se enumeran en el archivo. Luego, generé un archivo CSV llamado 'ETL_movies_main.csv' para servir como archivo base para transformaciones posteriores.
- Creé el archivo 'ETL_movies_collection.ipynb'. En este archivo, cargué el archivo 'ETL_movies_main.csv' y retuve solo las columnas 'Movie_id' y 'belongs_to_collection'. Posteriormente, realicé las transformaciones necesarias. Finalmente, generé un nuevo archivo CSV llamado 'ETL_movies_collection.csv'.
- Creé el archivo 'ETL_movies_genres.ipynb'. En este archivo, cargué el archivo 'ETL_movies_main.csv' y retuve solo las columnas 'Movie_id' y 'genres'. Posteriormente, realicé las transformaciones necesarias. Finalmente, generé dos nuevos archivos CSV llamados 'ETL_movies_genres.csv' y 'ETL_movies_genres_grouped.csv'.
- Creé el archivo 'ETL_movies_languages.ipynb'. En este archivo, cargué el archivo 'ETL_movies_main.csv' y retuve solo las columnas 'Movie_id' y 'spoken_languages'. Posteriormente, realicé las transformaciones necesarias. Finalmente, generé un nuevo archivo CSV llamado 'ETL_movies_languages.csv'.
- Creé el archivo 'ETL_movies_pcompanies_pcountries.ipynb'. En este archivo, cargué el archivo 'ETL_movies_main.csv' y retuve solo las columnas 'Movie_id', 'production_companies' y 'production_countries'. Posteriormente, realicé las transformaciones necesarias. Finalmente, generé un nuevo archivo CSV llamado 'ETL_movies_productions.csv'.
- Creé el archivo 'ETL_movies_credits.ipynb'. En este archivo, cargué el archivo CSV llamado 'credits.csv', que fue el segundo archivo fuente. Luego, comencé las transformaciones y generé dos archivos CSV llamados 'ETL_credits_cast.csv' y 'ETL_credits_crew.csv'.

## Desarrollo de la API

Con los datos divididos en ocho archivos, comencé el proceso de definir seis funciones. Para cada función, utilicé el archivo CSV respectivo creado durante la fase de ETL. Hice ajustes y transformaciones a estos archivos CSV de ETL para alinearlos con los requisitos de cada función y optimizar su rendimiento dentro de FastAPI y Render.

- Para la función uno, 'peliculas_idioma,' cargué el archivo 'ETL_movies_languages.csv', realicé pruebas de DataFrame, hice ajustes apropiados y luego diseñé la función. Después de eso, generé un nuevo archivo 'movies_df_func1.csv' para servir como el DatFrame que alimenta la función 1.
- Para la función dos, 'peliculas_duracion,' cargué el archivo 'ETL_movies_main.csv', realicé pruebas de DataFrame, hice ajustes apropiados y luego diseñé la función. Después de eso, generé un nuevo archivo 'movies_df_func2.csv' para servir como el DataFrame que alimenta la función 2.
- Para la función tres, 'franquicia,' cargué los archivos 'ETL_movies_main.csv' y 'ETL_movies_collection.csv', realicé pruebas de DataFrames, hice ajustes apropiados, fusioné los dos archivos en uno solo y luego diseñé la función. Después de eso, generé un nuevo archivo 'movies_df_func3.csv' para servir como el DataFrame que alimenta la función 3.
- Para la función cuatro, 'peliculas_pais,' cargué el archivo 'ETL_movies_productions.csv', realicé pruebas de DataFrame, hice ajustes apropiados y luego diseñé la función. Después de eso, generé un nuevo archivo 'movies_df_func4.csv' para servir como el DataFrame que alimenta la función 4.
- Para la función cinco, 'productoras_exitosas,' cargué los archivos 'ETL_movies_main.csv' y 'ETL_movies_productions.csv', realicé pruebas de DataFrames, hice ajustes apropiados, fusioné los dos archivos en uno solo y luego diseñé la función. Después de eso, generé un nuevo archivo 'movies_df_func5.csv' para servir como el DataFrame que alimenta la función 5.
- Para la función seis, 'get_director,' cargué los archivos 'ETL_movies_main.csv' y 'ETL_credits_crew.csv', realicé pruebas de DataFrames, hice ajustes apropiados, fusioné los dos archivos en uno solo y luego diseñé la función. Después de eso, generé un nuevo archivo 'movies_df_func6.csv' para servir como el DataFrame que alimenta la función 6.
- Finalmente, creé el archivo 'main.py' y construí el cuerpo de la API.

## EDA

En el Análisis Exploratorio de Datos (EDA), comencé cargando los datos desde los archivos CSV generados en la fase de Extracción, Transformación y Carga (ETL). Realicé varias transformaciones para ajustar y combinar los DataFrames, lo que resultó en un DataFrame final llamado 'df_final'. Posteriormente, llevé a cabo el siguiente análisis:

- Distribución de datos
- Evaluación de asimetría (skewness)
- Películas con mayores ingresos
- Películas con mayor presupuesto
- Incremento de popularidad de las películas a lo largo de los años
- Compañías con más películas producidas
- Compañías más rentables
- Análisis de correlación
- Actores principales por apariciones en películas

## Machine Learning

Para la función de Aprendizaje Automático (Machine Learning) llamada 'recomendacion', cargué los archivos 'ETL_movies_main.csv' y 'df_ml_genres_grouped.csv', realicé pruebas de DataFrames, hice ajustes y transformaciones adecuadas, fusioné los dos archivos en uno solo y creé el archivo 'df_ml.csv'.
Con el DataFrame "df_ml" listo, comencé a probar dos Modelos de Aprendizaje Automático, 'dbscan' y 'cosine_similarity'.
Después de realizar pruebas, opté por utilizar el modelo 'cosine_similarity' y lo integré en el archivo 'main.py'.

## API y Video

Aquí comparto dos enlaces, el primero a mi API desplegada en Render, y el segundo a un video que muestra mi API desplegada exitosamente en Render y siendo probada.

- [Probar API](https://ml-ops-nicolasyapur.onrender.com)
- [Ver Video](https://drive.google.com/file/d/18MQcUIgLEWf9Jd8glf7hqRUjE89EJ20d/view?usp=sharing)

## Archivos Adicionales

- Agregué un archivo de requerimientos (requirements) para especificar las bibliotecas a utilizar al desplegar en Render.
- Agregué un archivo .gitignore para ignorar archivos innecesarios y evitar que se carguen en GitHub.
- 'credits.csv' y 'movies_dataset.csv' son los datos proporcionados para desarrollar el proyecto.
- 'credits.csv' excedió el límite de tamaño de GitHub y se agregó a gitignore.
