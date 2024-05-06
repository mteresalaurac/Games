from fastapi import FastAPI
app = FastAPI()


import pandas as pd
#Importo el archivo de GAMES
games=pd.read_csv("Archivos_Comprimidos/games.csv",encoding="latin-1")

#Importo el archivo de REVIEWS
reviews_prueba= pd.read_parquet("Archivos_Comprimidos/reviews_final.parquet")

#Importo el archivo de ITEMS
items=pd.read_parquet("Archivos_Comprimidos/items.parquet")

#DataFrame joineado para funciones 1) y 2). Voy a unir games con items
items['item_id'] = items['item_id'].astype(float) #Necesito igualar el tipo de dato para poder joinear las tablas 
df= pd.merge(items, games, on='item_id', how='inner')

@app.get("/")
async def ruta_prueba():
    return "BOCA"



#Primera Funcion
@app.get("/PlayTimeGenre")
async def PlayTimeGenre( genero : str ):
    # 1) Paso toda al columna de generos a minuscula
    df['genres'] = df['genres'].str.lower()
    
    # 2) Filtro los valores que contienen el genero que me interesa
    genero="casual" # a modo prueba
    df_filtrado = df[df.filter(like='genres').apply(lambda x: x.str.contains(genero)).any(axis=1)] 
    
    #3) Agrupo los valores por año.
    df_ordenado=df_filtrado[["date","horas"]].groupby(["horas"]).sum().sort_values(by='horas',ascending=False)
    
    #4) Reseteo con indices numericos
    df_ordenado.reset_index(inplace=True) #Agrego el indice para ver las posiciones
    
    #5) Imprimo resultado de funcion
    print(f"Cantidad de horas jugadas en dicho año: {int(df_ordenado.horas.iloc[0])}")
    return


    
    
    
    
    
    
    
    
    
    
    return "BOCA"