import pandas as pd
from API.funciones import UserForGenre,SentimentAnalysis,RecommendedGames
from fastapi import FastAPI

#Inicializamos
app = FastAPI()
app.title='Steam Games'
@app.get("/", tags=['Inicio'])
def bienvenida():
   return 'Bienvenidos'

@app.get("/user_for_genre/{genero}", tags=['Consultas'])
async def user_for_genre (genero:str):
    diccionario=UserForGenre(genero)
    return diccionario

@app.get("/sentiment_analysis/{developer}", tags=['Consultas'])
async def sentiment_analysis (developer:str):
    dicc=SentimentAnalysis (developer)
    return dicc

@app.get("/recommended_games/{id}", tags=['Sistema de recomendación'])
async def recomendacion_juego(id: int, top_n: int = 5):
    # Llamar directamente a la función RecomendacionJuego con los parámetros proporcionados
    recommended_games = RecommendedGames(id, top_n)
        
    # Devolver los resultados como respuesta de la API
    return {"JuegosRecomendados": recommended_games.to_list()}