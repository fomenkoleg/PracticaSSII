import pandas as pd
import sqlite3





def ejercicio2():

    conn = sqlite3.connect('users_data_online.db')
    cursor = conn.cursor()

    # preprocessing

    query_users = "SELECT * FROM user_data_online WHERE username IS NOT 'None' AND tel_num IS NOT 'None' AND hash_password IS NOT 'None' AND pass_complexity IS NOT 'None' AND province IS NOT 'None' AND permisos IS NOT 'None' AND emails_total IS NOT 'None' AND emails_phishing IS NOT 'None' AND emails_clicados IS NOT 'None';"
    query_ips = "SELECT * FROM users_ips_fechas WHERE username_access IN (SELECT username FROM user_data_online WHERE username IS NOT 'None' AND tel_num IS NOT 'None' AND hash_password IS NOT 'None' AND pass_complexity IS NOT 'None' AND province IS NOT 'None' AND permisos IS NOT 'None' AND emails_total IS NOT 'None' AND emails_phishing IS NOT 'None' AND emails_clicados IS NOT 'None');"
    query_webs = "SELECT * FROM legal_data_online;"

    df_users = pd.read_sql_query(query_users, conn)
    df_fechas = pd.read_sql_query(query_ips, conn)
    df_legal = pd.read_sql_query(query_webs, conn)

    # pregunta 1
    numero_muestras_user = df_users['username'].count()
    print("Numero de muestras usuarios: ", numero_muestras_user)

    numero_muestras_ips = df_fechas['id'].count()
    print("Numero de muestras fechas-ips: ", numero_muestras_ips)

    numero_muestras_webs = df_legal['web'].count()
    print("Numero de muestras webs: ", numero_muestras_webs)
    print()

    # pregunta 2
    df_fechas['fecha'] = pd.to_datetime(df_fechas['fecha'])
    print("La media de las fechas es: "+ str(df_fechas['fecha'].mean()))
    print("La desviación estándar de las fechas es: " + str(df_fechas['fecha'].std()))

    # pregunta 3
    #print(df_fechas.groupby('username_access').count())
    print("Media de fechas por usuario:")
    print(df_fechas.groupby('username_access').count().mean()['fechas'])
    print("Variación de fechas/IPs por usuario:")
    print(df_fechas.groupby('username_access').count().std()['fechas'])



ejercicio2()