import sqlite3
import pandas as pd

def calcular_puntuacion(cookies, aviso, proteccion):
    return cookies + aviso + proteccion

def top_webs(top_x):
    conn = sqlite3.connect('users_data_online.db')
    answer = ''
    # Consulta para obtener los datos de la tabla de legal
    query_webs = 'SELECT web, creacion, cookies, aviso, proteccion FROM legal_data_online;'
    df_webs = pd.read_sql_query(query_webs, conn)


    #top max == 14
    puntuaciones = []
    for index, row in df_webs.iterrows():
        num = calcular_puntuacion(row['cookies'], row['aviso'], row['proteccion'])
        puntuaciones.append(num)

    df_webs['puntuacion'] = puntuaciones

    # Filtrar las páginas web desactualizadas
    desactualizadas = df_webs[df_webs['puntuacion'] != 3]

    #Ordenar las webs 
    desactualizadas = desactualizadas.sort_values(by=['puntuacion', 'creacion'], ascending=[True, True])

    return desactualizadas.head(top_x).to_dict(orient='records')





