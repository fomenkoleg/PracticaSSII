import pandas as pd
import sqlite3


def ejercicio2():

    # Conectamos con la base de datos
    conn = sqlite3.connect('users_data_online.db')

    # CONSULTAS SIN FILTRADO

    # Hacemos las consultas para obtener la información necesaria de las tablas de usuarios e IPs-fechas
    query_users = "SELECT * FROM user_data_online;"
    query_ips = "SELECT * FROM users_ips_fechas WHERE username_access IN (SELECT username FROM user_data_online);"

    #Creamos los DataFrames de pandas con los resultados de las consultas
    df_users = pd.read_sql_query(query_users, conn)
    df_fechas = pd.read_sql_query(query_ips, conn)

    # pregunta 1
    print("DATOS SIN FILTRAR NONE")
    print()
    print("###############################################################################")
    print()
    print("Numero de muestras de usuarios después del filtrado: ")
    print(df_users['username'].count())
    print("Numero de muestras de fechas-ips después del filtrado: ")
    print(df_fechas['id'].count())
    print()

    # pregunta 2
    print("Media de fechas por usuario:")
    print(df_fechas.groupby('username_access').count().mean()['fecha'])
    print("Desviación estándar de fechas por usuario:")
    print(df_fechas.groupby('username_access').count().std()['fecha'])
    print()

    # pregunta 3
    print("Media de IPs por usuario:")
    print(df_fechas.groupby('username_access').count().mean()['ip_address'])
    print("Desviación estándar de IPs por usuario:")
    print(df_fechas.groupby('username_access').count().std()['ip_address'])
    print()

    # pregunta 4
    print("La media de los emails recibidos de phishing por usuario: ")
    print(df_users['emails_phishing'].mean())
    print()

    # pregunta 5
    print("El valor mínimo de los emails recibidos en total: ")
    print(df_users['emails_total'].min())
    print("El valor máximo de los emails recibidos en total: ")
    print(df_users['emails_total'].max())
    print()

    # pregunta 6
    query_admin = "SELECT * FROM user_data_online WHERE permisos IS 1 ;"
    administradores = pd.read_sql_query(query_admin, conn)

    print("Valor mínimo de emails de phishing clicados por usuario con permisos de administrador: ")
    print(administradores['emails_clicados'].min())
    print("Valor máximo de emails de phishing clicados por usuario con permisos de administrador: ")
    print(administradores['emails_clicados'].max())
    print()
    print()


    # Consultas + preprocessing
    print("DATOS FILTRANDO NONE")
    print()
    print("###############################################################################")
    print()
    # En las consultas eliminamos las entradas que tengan algún campo a none
    query_users_filter = "SELECT * FROM user_data_online WHERE username IS NOT 'None' AND tel_num IS NOT 'None' AND hash_password IS NOT 'None' AND pass_complexity IS NOT 'None' AND province IS NOT 'None' AND permisos IS NOT 'None' AND emails_total IS NOT 'None' AND emails_phishing IS NOT 'None' AND emails_clicados IS NOT 'None';"
    query_ips_filter = "SELECT * FROM users_ips_fechas WHERE username_access IN (SELECT username FROM user_data_online WHERE username IS NOT 'None' AND tel_num IS NOT 'None' AND hash_password IS NOT 'None' AND pass_complexity IS NOT 'None' AND province IS NOT 'None' AND permisos IS NOT 'None' AND emails_total IS NOT 'None' AND emails_phishing IS NOT 'None' AND emails_clicados IS NOT 'None');"

    # Creamos los respectivos DataFrames
    df_users = pd.read_sql_query(query_users_filter, conn)
    df_fechas = pd.read_sql_query(query_ips_filter, conn)

    # CON LOS VALORES FILTRADOS

    # pregunta 1
    print("Numero de muestras de usuarios después del filtrado: ")
    print(df_users['username'].count())
    print("Numero de muestras de fechas-ips después del filtrado: ")
    print(df_fechas['id'].count())
    print()

    # pregunta 2
    print("Media de fechas por usuario:")
    print(df_fechas.groupby('username_access').count().mean()['fecha'])
    print("Desviación estándar de fechas por usuario:")
    print(df_fechas.groupby('username_access').count().std()['fecha'])
    print()

    # pregunta 3
    print("Media de IPs por usuario:")
    print(df_fechas.groupby('username_access').count().mean()['ip_address'])
    print("Desviación estándar de IPs por usuario:")
    print(df_fechas.groupby('username_access').count().std()['ip_address'])
    print()

    # pregunta 4
    print("La media de los emails recibidos de phishing por usuario: ")
    print(df_users['emails_phishing'].mean())
    print()

    # pregunta 5
    print("El valor mínimo de los emails recibidos en total: ")
    print(df_users['emails_total'].min())
    print("El valor máximo de los emails recibidos en total: ")
    print(df_users['emails_total'].max())
    print()

    # pregunta 6
    query_admin = "SELECT * FROM user_data_online WHERE permisos IS 1 AND username IS NOT 'None' AND tel_num IS NOT 'None' AND hash_password IS NOT 'None' AND pass_complexity IS NOT 'None' AND province IS NOT 'None' AND permisos IS NOT 'None' AND emails_total IS NOT 'None' AND emails_phishing IS NOT 'None' AND emails_clicados IS NOT 'None';"
    administradores = pd.read_sql_query(query_admin, conn)

    print("Valor mínimo de emails de phishing clicados por usuario con permisos de administrador: ")
    print(administradores['emails_clicados'].min())
    print("Valor máximo de emails de phishing clicados por usuario con permisos de administrador: ")
    print(administradores['emails_clicados'].max())

ejercicio2()