#Se importan las librerias a utilizar
import pandas as pd
from typing import Dict, Any, List

games_pkl_path=r'C:\Users\Nahir\Desktop\Steamgames_API_ML\API\PKL\Consultas\games.pkl'
items_pkl_path=r'C:\Users\Nahir\Desktop\Steamgames_API_ML\API\PKL\Consultas\items.pkl'
review_pkl_path=r'C:\Users\Nahir\Desktop\Steamgames_API_ML\API\PKL\Consultas\review.pkl'
games_ml_pkl_path = r'C:\Users\Nahir\Desktop\Steamgames_API_ML\API\PKL\ML\games_ml.pkl'
cosine_sim_svd_pkl_path = r'C:\Users\Nahir\Desktop\Steamgames_API_ML\API\PKL\cosine_sim_svd.pkl'


def UserForGenre(genero: str) -> Dict[str, Any]:
    '''
    Función que recibe un género como parámetro 
    y devuelve el usuario con más horas jugadas para ese género, 
    junto a la cantidad de horas jugadas.
    '''
    df_games = pd.read_pickle(games_pkl_path)
    df_items2 = pd.read_pickle(items_pkl_path)
    try:
        #Se filtran los juegos por el género dado
        game_genre = df_games[df_games['genres'].apply(lambda x:genero in x)]
        #Se obtienen los IDs de los juegos del género dado
        game_id = game_genre['app_name'].tolist()
        # Filtrar los elementos por los IDs de los juegos del género dado
        item_genre= df_items2[df_items2['item_name'].isin (game_id)]
        # Fusionar 'item_genre' con 'df_games' utilizando el ID del juego ('id')
        item_genre = item_genre.merge(game_genre[['app_name', 'release_date']], left_on='item_name', right_on='app_name', how='left')
        #Se elimina la columna 'id' extra, en caso de haber sido generada por el merge
        item_genre = item_genre.drop('app_name', axis=1)
        #Se agrupa por usuario y se suma las horas jugadas
        user_playtime = item_genre.groupby('user_id')['playtime_forever'].sum().reset_index()
        #Se encuentra el usuario con más horas jugadas
        max_playtime_user = user_playtime.loc[user_playtime['playtime_forever'].idxmax()]
        max_playtime_user_id = max_playtime_user['user_id']
        #Se filtra los elementos del usuario con más horas jugadas
        max_playtime_user_items = item_genre[item_genre['user_id'] == max_playtime_user_id]
        #Se obtiene la acumulación de horas jugadas por año para el usuario
        playtime_by_year = (
            max_playtime_user_items.groupby(max_playtime_user_items['release_date'].dt.year)
            ['playtime_forever'].sum().reset_index().rename(columns={'release_date': 'Año', 'playtimeforever': 'Horas'})
            )
        #Se crea la respuesta con el usuario y las horas jugadas por año
        response = {
            "Usuario con más horas jugadas para Género " + genero: max_playtime_user_id,
            "Horas jugadas": playtime_by_year.to_dict(orient='records')
        }
        return response
    except:
        return {
            'Error': f'No se encontraron usarios para el género {genero}'
        }

def SentimentAnalysis (developer: str):
    '''
    Función que recibe el nombre de la empresa desarrolladora como parámetro
    y devuleve un diccionario con el nombre de la desarrolladora como llave
    y una lista con la cantidad total de registros de reseñas de usuarios
    categorizados en Positive, Neutral y Negative.
    '''
    df_games = pd.read_pickle(games_pkl_path)
    df_items2 = pd.read_pickle(items_pkl_path)
    df_reviews = pd.read_pickle(review_pkl_path)
    try:
        #Se filtran los juegos de la empresa desarrolladora
        juegos_empresa = df_games[df_games['developer'] == developer]
        #Se obtienen los nombres de los juegos de la empresa desarrolladora
        nombres_juegos_empresa = juegos_empresa['app_name'].tolist()
        #Se filtran las reseñas por los nombres de los juegos de la empresa desarrolladora
        reviews_empresa = df_reviews[df_reviews['item_id'].isin(df_items2[df_items2['item_name'].isin(nombres_juegos_empresa)]['item_id'])]
        df_items2[df_items2['item_name'].isin(nombres_juegos_empresa)]['item_id']
        #Se cuentan las ocurrencias de cada tipo de sentimiento
        sentiment_counts = reviews_empresa['sentiment_analysis'].value_counts()
        #Se crea un diccionario con los recuentos de sentimientos
        sentiment_dict = {
            developer: {
            'Negative': sentiment_counts.get(0, 0),
            'Neutral': sentiment_counts.get(1, 0),
            'Positive': sentiment_counts.get(2, 0)
                }
            }
        return sentiment_dict
    except:{
        'Error':f'No se encontraron reseñas para la empresa desarrolladora {developer}'
    }


def RecomendacionJuego( id, top_n =5 ):
    '''
    Función que recibe el id de un juego como parámetro
    y devuelve los nombres de 5 juegos recomendados por similitud
    '''
    df_g_ML = pd.read_pickle(games_ml_pkl_path)
    cosine_sim_svd = pd.read_pickle(cosine_sim_svd_pkl_path)
    try:
        #Se buscan el id en el DataFarme
        game_index =df_g_ML[df_g_ML['id'] == id].index[0]
        #Se obtiene la similitud con otros juegos y se enumera
        similar_games = list(enumerate(cosine_sim_svd[game_index]))
        #Se ordenan los juegos similares, por similitud de mayor a menor
        similar_games = sorted(similar_games, key=lambda x: x[1], reverse=True)
        #Se seleccionan los juegos más similares (excluyendo el propio juego)
        similar_games = similar_games[1:top_n+1]
        #Se obtienen los indices de los juegos recomendados
        similar_game_indices = [i[0] for i in similar_games]
        #Se obtienen los nombres de los juegos recomendados
        recommended_games =df_g_ML['app_name'].iloc[similar_game_indices]
        return recommended_games
    except:{
        'Error':f'No se encontraron recomendaciones para el juego con id {id}'
    }