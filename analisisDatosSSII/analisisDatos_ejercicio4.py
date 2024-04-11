import sqlite3
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def ejercicio4_1():
    answer = ''
    # Conectamos con la base de datos
    conn = sqlite3.connect('users_data_online.db')

    # Parte 1
    # Se hacen las consultas para obtener los datos de usuarios normales y admins
    query_ips_normal = "SELECT * FROM users_ips_fechas WHERE username_access IN (SELECT username FROM user_data_online  WHERE permisos IS 0);"
    query_ips_admin = "SELECT * FROM users_ips_fechas WHERE username_access IN (SELECT username FROM user_data_online  WHERE permisos IS 1);"
    # Y se crean los DataFrames correspondientes
    df_ips_normal = pd.read_sql_query(query_ips_normal, conn)
    df_ips_admin = pd.read_sql_query(query_ips_admin, conn)

    # Convertir la columna "fecha" al tipo datetime
    df_ips_normal['fecha'] = pd.to_datetime(df_ips_normal['fecha'], format="%d/%m/%Y")
    df_ips_admin['fecha'] = pd.to_datetime(df_ips_admin['fecha'], format="%d/%m/%Y")

    # Ordenar los DataFrames segun el nombre de usuario y la fecha
    df_ips_normal = df_ips_normal.sort_values(by=['username_access', 'fecha'])
    df_ips_admin = df_ips_admin.sort_values(by=['username_access', 'fecha'])

    # Calcular la diferencia en dias de las fechas consecutivas, por usuario
    df_ips_normal['diferencia'] = pd.to_numeric(df_ips_normal.groupby('username_access')['fecha'].diff().dt.days)
    df_ips_admin['diferencia'] = pd.to_numeric(df_ips_admin.groupby('username_access')['fecha'].diff().dt.days)

    # Mostramos los valores obtenidos
    answer+=("La media de tiempo medio entre cambios de contraseña por usuario normal (en días): ")+'\n\n'
    medias_ips_normal = df_ips_normal.groupby('username_access')['diferencia'].mean()
    answer+=(medias_ips_normal.to_string())+'\n\n'

    answer+=("La media de tiempo medio entre cambios de contraseña por usuario administrador (en días): ")+'\n\n'
    medias_ips_admin = df_ips_admin.groupby('username_access')['diferencia'].mean()
    answer+=(medias_ips_admin.to_string())+'\n\n'

    # Crear una gráfica de barras para comparar los tiempos medios entre los cambios de contraseña
    plt.figure(figsize=(25, 16))

    plt.subplot(1, 2, 1)
    plt.title('Tiempo medio trascurrido en días ara usuarios normales')
    medias_ips_normal.plot(kind='bar', x='username_access', y='', color='aqua')

    plt.subplot(1, 2, 2)
    plt.title('Tiempo medio trascurrido en días ara usuarios admin')
    medias_ips_admin.plot(kind='bar', x='username_access', y='Tiempo medio trascurrido', color='magenta')

    plt.savefig("static/images/grafico1.png")

    #plt.show()
    return answer

def ejercicio4_2():

    conn = sqlite3.connect('users_data_online.db')
    # Hacer consultas de usuarios con contraseñas inseguras y crear DataFrame
    query_inseguros = 'SELECT username, emails_clicados, emails_phishing FROM user_data_online WHERE pass_complexity IS 0 AND emails_clicados IS NOT "None" AND emails_phishing IS NOT "None";'
    df_inseguros = pd.read_sql_query(query_inseguros, conn)

    # Calcular probabilidad de éxito para ataques de phishing
    df_inseguros['probabilidad_phishing'] = (df_inseguros['emails_clicados']/df_inseguros['emails_phishing'])*100
    df_inseguros.fillna(0, inplace=True)
    df_inseguros.sort_values(by=['probabilidad_phishing'], inplace=True, ascending=False)

    # Quitar columnas que no se mostrarán en la gráfica
    df_inseguros.drop(['emails_clicados', 'emails_phishing'], axis=1, inplace=True)


    # Limitar DataFrame a los primeros 10 usuarios
    # df_inseguros = df_inseguros.head(10)


    # Crear gráfico de barras correspondiente
    df_inseguros.plot(kind='bar', x='username', color='aqua')
    plt.title("Probabilidad de éxito de ataque de phishing")
    plt.xlabel("Usuario")
    plt.ylabel("Probabilidad de éxito")
    plt.legend()
    plt.tight_layout()
    plt.savefig("static/images/grafico2.png")
    #plt.show()
    return df_inseguros.head(10).to_string()

def ejercicio_headnum(num):

    conn = sqlite3.connect('users_data_online.db')
    query_inseguros = 'SELECT username, emails_clicados, emails_phishing FROM user_data_online WHERE pass_complexity IS 0 AND emails_clicados IS NOT "None" AND emails_phishing IS NOT "None";'
    df_inseguros = pd.read_sql_query(query_inseguros, conn)
    df_inseguros['probabilidad_phishing'] = (df_inseguros['emails_clicados']/df_inseguros['emails_phishing'])*100
    df_inseguros.fillna(0, inplace=True)
    df_inseguros.sort_values(by=['probabilidad_phishing'], inplace=True, ascending=False)
    df_inseguros.drop(['emails_clicados', 'emails_phishing'], axis=1, inplace=True)

    df_inseguros.plot(kind='bar', x='username', color='aqua')
    plt.title("Probabilidad de éxito de ataque de phishing")
    plt.xlabel("Usuario")
    plt.ylabel("Probabilidad de éxito")
    plt.legend()
    plt.tight_layout()
    plt.savefig("static/images/grafico2.png")
    if num > df_inseguros.shape[0]:
        return df_inseguros
    elif num < -1 or num == 0:
        return None
    return df_inseguros.head(num)

def ejercicio4_3():

    conn = sqlite3.connect('users_data_online.db')
    answer=''
    # Realizar consultas para obtener datos de la tabla de legal
    query_webs = 'SELECT web, cookies, aviso, proteccion FROM legal_data_online;'
    df_webs = pd.read_sql_query(query_webs, conn)

    # Calcular la cantidad de políticas desactualizadas
    df_webs['desactualizadas'] = df_webs[['cookies', 'aviso', 'proteccion']].apply(lambda row: sum(row == 0), axis=1)

    # Para que en la gráfica aparezca con el nombre del sitio web
    df_webs = df_webs.set_index('web')
    answer+=(df_webs.to_string())+'\n'

    # Ordenar las webs según el número de políticas desactualizadas y quedarse con los 5 primeros
    df_webs.sort_values(by=['desactualizadas'], inplace=True, ascending=False)
    primeros_cinco = df_webs.head(5)

    # C rear gráfico de barras correspondiente
    primeros_cinco.plot(kind='bar')
    plt.title('Políticas desactualizadas por página web')
    plt.xlabel('Página Web')
    plt.ylabel('Estado')
    plt.legend()

    plt.tight_layout()
    plt.savefig("static/images/grafico3.png")
    #plt.show()
    return answer

def ejercicio4_4():

    conn = sqlite3.connect('users_data_online.db')
    answer = ''
    # Consulta para obtener los datos de la tabla de legal
    query_webs = 'SELECT web, creacion, cookies, aviso, proteccion FROM legal_data_online;'
    df_webs = pd.read_sql_query(query_webs, conn)

    # Creación de columna para indicar si se cumplen las políticas de seguridad
    df_webs['satisface'] = (df_webs['cookies'] == 1) & (df_webs['aviso'] == 1) & (df_webs['proteccion'] == 1)

    # Agrupar las webs sgún el año de creación y si satisfacen las políticas, contando el numero de webs de cada categoría
    df_webs_agrupado_dos_columnas= df_webs.groupby(['creacion', 'satisface']).size().unstack()
    answer+=str(df_webs_agrupado_dos_columnas)+'\n'

    # Gráfico de barras correspondiente
    df_webs_agrupado_dos_columnas.plot(kind='bar')
    plt.title('Webs por año que cumplen las políticas de seguridad')
    plt.xlabel('Año creación')
    plt.ylabel('Número de sitios web')
    plt.legend(['No se cumple', 'Se cumple'])
    plt.tight_layout()
    plt.savefig("static/images/grafico4.png")
    #plt.show()
    return answer

def ejercicio_50percent(mitad):
    df = ejercicio_headnum(-1)
    if mitad == 1:
        df = df[df['probabilidad_phishing'] <= 50]
    elif mitad == 2:
        df = df[df['probabilidad_phishing'] > 50]
    return df

if __name__ == '__main__':
    ejercicio4_1()
    ejercicio4_2()
    ejercicio4_3()
    ejercicio4_4()
    ejercicio_50percent(2)
    ejercicio_headnum(10)