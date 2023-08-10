############################################# LIBRERIAS #########################################

import pandas as pd
import numpy as np
from pandas import json_normalize
from fastapi import FastAPI,Body

app = FastAPI()


######################################## CARGANDO DATASETS #########################################

# Para Funcion 1
movies_df_func1 = pd.read_csv("movies_df_func1.csv")

# Para Funcion 2
movies_df_func2 = pd.read_csv("movies_df_func2.csv")

# Para Funcion 3
movies_df_func3 = pd.read_csv("movies_df_func3.csv")

# Para Funcion 4
movies_df_func4 = pd.read_csv("movies_df_func4.csv")

# Para Funcion 5
movies_df_func5 = pd.read_csv("movies_df_func5.csv")

# Para Funcion 6
movies_df_func6 = pd.read_csv("movies_df_func6.csv")

# Para ML

df_ml = pd.read_csv("df_ml.csv")





###################################### Funcion 1 ###########################################

# Se ingresa un idioma (como están escritos en el dataset, no hay que traducirlos!).
# Debe devolver la cantidad de películas producidas en ese idioma.


@app.get("/peliculas_idioma")
def peliculas_idioma(idioma: str):
    if idioma in movies_df_func1["short_language"].unique():
        seleccion = movies_df_func1.loc[movies_df_func1["short_language"] == idioma, ["short_language"]]
        respuesta = seleccion.shape[0]
        return {"message": f"La cantidad de Peliculas en el idioma {idioma} es {respuesta}"}
    else:
        return {"message": "El Idioma no se encuentra en la lista o El dato ingresado no es correcto, intenta escribir de la siguiente forma -> Ej: 'English'='en'"}

    


###################################### Funcion 2 ###########################################

#Se ingresa una pelicula. Debe devolver la duracion y el año.

@app.get("/peliculas_duracion")
def peliculas_duracion(movie_title: str):
    if movie_title in movies_df_func2["title"].values:
        seleccion = movies_df_func2[movies_df_func2["title"] == movie_title]
        runtime_ = seleccion.loc[seleccion.index[0], "runtime"]
        release_year_ = seleccion.loc[seleccion.index[0], "release_year"]
        return {
            "message": f"La película {movie_title} tiene una duración de {runtime_} minutos y se estrenó en el año {release_year_}"
        }
    else:
        return {
            "message": "La película no está en la lista o intenta escribir el nombre de la siguiente forma -> Ej: 'Toy Story'"
        }




###################################### Funcion 3 ###########################################

#Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio


@app.get("/franquicia")
def franquicia(nombre_franquicia: str):
    if nombre_franquicia in movies_df_func3["collection_name"].unique():
        filtro = movies_df_func3.loc[movies_df_func3["collection_name"] == nombre_franquicia]
        cantidad_pelis = filtro["Movie_id"].count()
        ganancia_total = filtro["revenue"].sum()
        ganancia_promedio = filtro["revenue"].mean()
        
        ganancia_total_formatted = "{:.2f}".format(ganancia_total)
        ganancia_promedio_formatted = "{:.2f}".format(ganancia_promedio)
        
        return f"La franquicia {nombre_franquicia} cuenta con {cantidad_pelis} peliculas, produjo una ganancia Bruta de {ganancia_total_formatted} y una ganancia Bruta promedio por pelicula de {ganancia_promedio_formatted}"
    else:
        return "La franquicia no existe en el catalogo o prueba escribiendo de la siguiente forma -> Ej: 'Toy Story Collection' "
    



###################################### Funcion 4 ###########################################

#Se ingresa un país (como están escritos en el dataset, no hay que traducirlos!), retornando la cantidad de peliculas producidas en el mismo.


@app.get("/nombre_pais")
def peliculas_pais(nombre_pais: str):
    if nombre_pais in movies_df_func4["country_name"].unique():
        filtro = movies_df_func4.loc[movies_df_func4["country_name"] == nombre_pais]
        cantidad_pelis_producidas = filtro["Movie_id"].count()
        return f"La cantidad de Peliculas producidas en {nombre_pais} es de {cantidad_pelis_producidas}"
    else:
        return "Nombre de Pais no esta en la lista o error de escritura intenta escribirlo de la siguiente forma -> Ej: 'Germany' "
    



###################################### Funcion 5 ###########################################

#Se ingresa la productora, entregandote el revunue total y la cantidad de peliculas que realizo.


@app.get("/productoras_exitosas")
def productoras_exitosas(nombre_productora: str):
    if nombre_productora in movies_df_func5["company_name"].unique():
        filtro = movies_df_func5.loc[movies_df_func5["company_name"] == nombre_productora]
        ganancia_productora = filtro["revenue"].sum()
        cantidad_pelis_productora = filtro["Movie_id"].count()
        return f"La productora {nombre_productora} produjo una ganancia total Bruta de {ganancia_productora} y realizo una cantidad de {cantidad_pelis_productora} peliculas"
    else:
        return "Nombre de Productora no esta en la lista o error de escritura intenta escribirlo de la siguiente forma -> Ej: 'Pixar Animation Studios' "
    



###################################### Funcion 6 ###########################################

#Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno.
#Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma,
# en formato lista.



@app.get("/peliculas_director")
def get_director(nombre_director):
    if nombre_director in movies_df_func6["name"].unique():
        director_movies = movies_df_func6[movies_df_func6["name"] == nombre_director]
        total_return = director_movies["return"].sum()
        
        movies_info = []
        for index, row in director_movies.iterrows():
            movie_info = {
                "Nombre Pelicula": row["title"],
                "Fecha de Estreno": row["release_date"],
                "Ganancia Bruta": row["return"],
                "Presupuesto": row["budget"],
                "Ganancia Neta": row["revenue"]
            }
            movies_info.append(movie_info)
        
        return {
            "Exito,Retorno Total": total_return,
            "Peliculas": movies_info
        }
    else:
        return "Director no esta en la lista o intenta escribir de la siguiente manera -> Ej:'George Lucas' "
    




###################################### MACHINE LEARNING MODEL ######################################


import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Combinando las columnas de genero en una
df_ml['genres'] = df_ml[['genero1', 'genero2', 'genero3']].apply(lambda row: ' '.join(row.dropna()), axis=1)

# Calcular la similitud
vectorizer = CountVectorizer().fit_transform(df_ml['genres'])
genre_similarity = cosine_similarity(vectorizer)

# Funcion Nico
@app.get("/main/")
def recomendacion(movie_title: str):
    top_n=5
    if movie_title not in df_ml['title'].values:
        return f"La pelicula ingresada no esta en el catalogo o esta mal escrita. Intenta escribiendo de la siguiente manera -> Ej: 'Star Wars'"
    
    movie_idx = df_ml[df_ml['title'] == movie_title].index[0]
    similar_movies_indices = genre_similarity[movie_idx].argsort()[-top_n-1:][::-1]  # Include the input movie itself
    similar_movie_titles = [df_ml['title'][idx] for idx in similar_movies_indices if df_ml['title'][idx] != movie_title]

    # Para que me devuelva siempre 5 Pelis
    if len(similar_movie_titles) < top_n:
        additional_movies = df_ml[~df_ml['title'].isin([movie_title] + similar_movie_titles)]['title'].sample(top_n - len(similar_movie_titles))
        similar_movie_titles.extend(additional_movies)
    
    return similar_movie_titles