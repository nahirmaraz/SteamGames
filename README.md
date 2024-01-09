# Machine Learning No Supervisado-API-SteamGames
### Objetivos
Este proyecto tiene como objetivo principal aplicar técnicas de Data Engineering a una base de datos de videojuegos, mejorando la calidad y preparación de los datos para su posterior uso en el entrenamiento de un modelo de Machine Learning. Se busca entrenar un modelo no supervisado con el propósito de recomendar videojuegos basándose en sus características claves. Además, se tiene la meta de desarrollar una API que exponga las funcionalidades del modelo entrenado, permitiendo a los usuarios enviar el nombre de un videojuego y recibir recomendaciones de juegos similares.
### Introducción:
Inicias tu carrera como Data Scientist en Steam, una plataforma multinacional de videojuegos. Tu primer desafío es resolver una problemática del negocio,  crear un sistema de recomendación de videojuegos para usuarios.Aplicá técnicas de Data Engineering para pulir los datos y entrená un modelo preciso de recomendación. También tendrás que desarrollar una API para disponibilizar los datos de la empresa y que los usuarios obtengan recomendaciones de videojuegos con un clic.
### Estructura del proyecto:
- [API/](https://github.com/nahirmaraz/SteamGames/tree/main/API): Contiene las funciones y los de datos necesarios para el desarrolo de la API .
    - [API/PKL/](https://github.com/nahirmaraz/SteamGames/tree/main/API/PKL): Contiene los Dataframes necesarios para la API,en formato PKL.
    - [API/main.py](https://github.com/nahirmaraz/SteamGames/blob/main/API/main.py): Código para la creación de los endpoints y la API.
- [Data/](https://github.com/nahirmaraz/SteamGames/tree/main/Data): Contiene los notebooks utilizados para el proceso de Extracción, Transformación y Carga de los datos de los distintos DataFrames, asi tambien como el EDA para el ML.
- [requeriments.txt](https://github.com/nahirmaraz/SteamGames/blob/main/requeriments.txt): Contiene las librerias que se utilizaron para el desarrollo de la API.
- [.gitignore](https://github.com/nahirmaraz/SteamGames/blob/main/.gitignore): Contiene las carpetas del proyecto que se ignoraron para subir al repositorio
### Desarrollo:
Se realizó un proceso de Data Engineering para limpiar y preparar los datos de las bases de datos dadas (output_steam_games, australian_users_items y australian_user_reviews). Esto incluye la eliminación de valores nulos, duplicados y de columnas innecesarias; la creación de columnas con información valiosa; la conversión de tipos de datos; el manejo de valores atípicos y la codificación de características categóricas. Las tareas mencionadas anteriormente se hicieron gracias al uso de la librería pandas.
Para el modelo de Machine Learning se seleccionaron las columnas reelevantes y luego se las vectorizó para crear una matriz TF-IDF utilizando la librería Scikit-Learn.TfidfVectorizer.Posteriormente se redujo la dimensionalidad de la matriz con Scikit-Learn.TruncatedSVD y se aplicó la similitud del coseno entre vectores con Scikit-Learn.cosine_similarity.Se implementó un endpoint utilizando FastAPI para exponer el modelo entrenado a través de una API. La API permite a los usuarios enviar el nombre de un videojuego y recibir 5 juegos recomendados por similitud de características.
También se realizaron cinco endpoints mas, que disponibilizan los datos de la empresa. El primero, ingresando el género, da como resultado el año con mas horas jugadas para dicho género.El segundo, con el género como parámetro, devuelve el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año. El tercero devuelve el top 3 de juegos mas recomendados por usuarios segun el año ingresado como parámetro.El cuarto da como resultado el top 3 de desarrolladoras con juegos menos recomendados por usuarios para el año dado.
El quinto, según la empresa desarrolladora ingresada, devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor positive, neutral y negative.
Los endpoints fueron disponibilizados con la libreria FastAPI, usando el decorador correspondiente para cada uno. Luego, para el deploy de la API, se utilizó la plataforma de Render.
### Conclusiones:
Debido a que el objetivo final era disponibilzar todo en una API, todo el tiempo se tuvo en cuenta el límite de tamaño de los archivos que ésta puede resibir. Por esto, en el tratamiento de los datos se eliminaban directamente los nulos que no aportaban información, en vez de rellenarlos. Igualmente nunca se pasó del 20% del dataset original, excepto el de games que tenia mas del 50% filas copletamente nulas inicialmente.
### Como usar la API:
- [API](https://steamgames-xyis.onrender.com)
- [Documentación](https://steamgames-xyis.onrender.com/docs)
- [UserForGenre - Ejemplo ](https://steamgames-xyis.onrender.com/user_for_genre/Indie)
- [SentimentAnalysis - Ejemplo ](https://steamgames-xyis.onrender.com/sentiment_analysis/Poolians.com)
- [RecommendedGames - Ejemplo](https://steamgames-xyis.onrender.com/recommended_games/761140.0?top_n=5)
### Bibliografía:
- Consignas del Proyecto >> [Repositorio](https://github.com/nahirmaraz/PI_ML_OPS)
- Datasets iniciales >> [Drive](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj)
- Diccionario de datos >> [Sheets](https://docs.google.com/spreadsheets/d/1-t9HLzLHIGXvliq56UE_gMaWBVTPfrlTf2D9uAtLGrk/edit)
- Criterios de la API >> [FastAPI](https://fastapi.tiangolo.com/)
- Deploy >> [Render](https://docs.render.com/free#free-web-services)

