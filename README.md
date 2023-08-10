#################  proyecto ML_OPS Henry-Bootcamp Nicolas Yapur  ############################

# Movie Recomendation System

"Given two CSV files containing information about movies, the purpose of this project is to create an API that offers six functions providing relevant information about the data. Additionally, the project includes a Machine Learning Recommendation System. This system takes a movie title as input and returns a list of the five most similar movies to the inputted one."

## Table of Contents

- Introduction
- ETL
- API development   
- EDA
- Machine Learning
- Video and API
- Extra Files

## Introduction

"This project is a part of the Henry Data Science Bootcamp (PI_ML_OPS). It serves as the first of three projects required to graduate from the Bootcamp and is divided into five main steps. The primary objective of this project is to successfully transform raw data files into relevant information presented in the format of six questions and a recommendation system.

The project's deliverable is a fully functional API built using FastAPI and deployed on Render. Throughout this project, we apply the knowledge acquired during the bootcamp in the fields of Data Engineering and Data Science to create a real-life-like project."


## ETL

The Extract Transform and Load consisted in making the following steps:

- I created the 'ETL_movies_main.ipynb' file. Within this file, I loaded the CSV named 'movies_dataset.csv' that was the first source file and performed six main transformations, which are enumerated in the file. Afterward, I generated a CSV file named 'ETL_movies_main.csv' to serve as the foundational file for subsequent transformations.
- I created the 'ETL_movies_collection.ipynb' file. Within this file, I loaded the 'ETL_movies_main.csv' file and retained only the 'Movie_id' and 'belongs_to_collection' columns for further transformations. Subsequently, I performed the necessary transformations. Finally, I generated a new CSV file named 'ETL_movies_collection.csv'. 
- I created the 'ETL_movies_genres.ipynb' file. Within this file, I loaded the 'ETL_movies_main.csv' file and retained only the 'Movie_id' and 'genres' columns for further transformations. Subsequently, I performed the necessary transformations. Finally, I generated two new CSV files named 'ETL_movies_collection.csv' and 'ETL_movies_genres_grouped.csv'.
- I created the 'ETL_movies_languages.ipynb' file. Within this file, I loaded the 'ETL_movies_main.csv' file and retained only the 'Movie_id' and 'spoken_languages' columns for further transformations. Subsequently, I performed the necessary transformations. Finally, I generated a new CSV file named 'ETL_movies_languages.csv'.
- I created the 'ETL_movies_pcompanies_pcountries.ipynb' file. Within this file, I loaded the 'ETL_movies_main.csv' file and retained only the 'Movie_id','production_companies' and 'production_countries' columns for further transformations. Subsequently, I performed the necessary transformations. Finally, I generated a new CSV file named 'ETL_movies_productions.csv'.
- I created the 'ETL_movies_credits.ipynb' file. Within this file, I loaded the CSV named 'credits.csv', that was the second source file. Afterward i began the transformations and generated two CSV files called 'ETL_credits_cast.csv' and 'ETL_credits_crew.csv'. 


## API development

With the data divided into eight files, I began the process of defining six functions. For each function, I utilized the respective CSV file created during the ETL phase. I made adjustments and transformations to these ETL CSV files to align them with the requirements of each function and to optimize their performance within FastAPI and Render.

- For function one, 'peliculas_idioma,' I loaded the 'ETL_movies_languages.csv' file, conducted DataFrame testing, made appropriate adjustments, and subsequently designed the function. Following that, I generated a new 'movies_df_func1.csv' file to serve as input for function 1.
- For function two, 'peliculas_duracion,' I loaded the 'ETL_movies_main.csv' file, conducted DataFrame testing, made appropriate adjustments, and subsequently designed the function. Following that, I generated a new 'movies_df_func2.csv' file to serve as input for function 2.
- For function three, 'franquicia,' I loaded the 'ETL_movies_main.csv' and 'ETL_movies_collection.csv' files, conducted DataFrames testing, made appropriate adjustments, merged the two files into one, and subsequently designed the function. Following that, I generated a new 'movies_df_func3.csv' file to serve as input for function 3.
- For function four, 'peliculas_pais,' I loaded the 'ETL_movies_productions.csv' file, conducted DataFrame testing, made appropriate adjustments, and subsequently designed the function. Following that, I generated a new 'movies_df_func4.csv' file to serve as input for function 4.
- For function five, 'productoras_exitosas,' I loaded the 'ETL_movies_main.csv' and 'ETL_movies_productions.csv' files, conducted DataFrames testing, made appropriate adjustments, merged the two files into one, and subsequently designed the function. Following that, I generated a new 'movies_df_func5.csv' file to serve as input for function 5.
- For function six, 'get_director,' I loaded the 'ETL_movies_main.csv' and 'ETL_credits_crew.csv' files, conducted DataFrames testing, made appropriate adjustments, merged the two files into one, and subsequently designed the function. Following that, I generated a new 'movies_df_func6.csv' file to serve as input for function 6.
- Finally I created the 'main.py' file and built the body of the API.


## EDA

In the Exploratory Data Analysis (EDA), I began by loading the data from the ETL CSV files. I performed several transformations to adjust and join the DataFrames, ultimately resulting in a final DataFrame named 'df_final.' Subsequently, I conducted the following analysis:

- Data distribution
- Evaluating skewness
- Movies with the highest incomes
- Movies with the highest budget
- Movies' popularity increment over the years
- Top companies with more produced movies
- Top profitable companies
- Correlation analysis
- Top actors by appearances in movies


## Machine Learning

- For the ML function called 'recomendacion,' I loaded the 'ETL_movies_main.csv' and 'df_ml_genres_grouped.csv' files, conducted DataFrames testing, made appropriate adjustments/transformations , merged the two files into one ans created and generated the 'df_ml.csv' file.
- With the DataFrame "df_ml" ready I began to try two Machine Learning Models, 'dbscan' and 'cosine_similarity'.
- After conducting testing, I opted to use the 'cosine_similarity' model in the 'main.py' file and integrated it accordingly.


## Video and API

Heere I share two links, the first to my API Deployed in Render, the second to a video showing my API succesfully deployed in Render and being tested.

-- [ Try API](https://ml-ops-nicoyapur.onrender.com/docs)
-- [ Watch Video](link)

Provide instructions on how to install and set up your project.


## Extra Files

- I added a requirements file to specify the libraries to use while deploying in Render.
- I added a .gitignore file to ignore unnecesary files and prevent them to be loaded to github.
- 'credits.csv' and 'movies_dataset.csv' where the data given to develop the project.
- 'credits.csv' exceeded the limit size of github and was added to gitignore.