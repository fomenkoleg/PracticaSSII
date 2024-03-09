import pandas as pd
import sqlite3

def ejercicio3():
    conn = sqlite3.connect('users_data_online.db')

    query_permisos_0 = "SELECT * FROM user_data_online WHERE permisos=0"
    query_permisos_1 = "SELECT * FROM user_data_online WHERE permisos=1"

    df_p0 = pd.read_sql_query(query_permisos_0, conn)
    df_p1 = pd.read_sql_query(query_permisos_1, conn)

    query_pass_sec = "SELECT * FROM user_data_online WHERE pass_complexity=true"
    query_pass_noSec = "SELECT * FROM user_data_online WHERE pass_complexity=false"

    df_pwd_sec = pd.read_sql_query(query_pass_sec, conn)
    df_pwd_nosec = pd.read_sql_query(query_pass_noSec, conn)

    print("PERMISOS DE USUARIO")

    # pregunta 1
    print("Numero de observaciones de emails phishing: ")
    print(df_p0['emails_phishing'].count())
    print()

    # pregunta 2
    print("Numero missings:")
    if df_p0['emails_phishing'].min() == 0:
        print(df_p0['emails_phishing'].value_counts()[0])
    else:
        print("0")
    print()

    # pregunta 3
    print("Mediana:")
    print(df_p0['emails_phishing'].median())
    print()

    # pregunta 4
    print("Media:")
    print(df_p0['emails_phishing'].mean())
    print()

    # pregunta 5
    print("Varianza:")
    print(df_p0['emails_phishing'].var())
    print()

    # pregunta 6
    print("Valor maximo:")
    print(df_p0['emails_phishing'].max())
    print()
    print("Valor minimo:")
    print(df_p0['emails_phishing'].min())
    print()

    print("########################################################################")
    print()
    print("PERMISOS DE ADMIN")

    # pregunta 1
    print("Numero de observaciones de emails phishing: ")
    print(df_p1['emails_phishing'].count())
    print()

    # pregunta 2
    print("Numero missings:")
    if df_p1['emails_phishing'].min() == 0:
        print(df_p1['emails_phishing'].value_counts()[0])
    else:
        print("0")
    print()

    # pregunta 3
    print("Mediana:")
    print(df_p1['emails_phishing'].median())
    print()

    # pregunta 4
    print("Media:")
    print(df_p1['emails_phishing'].mean())
    print()

    # pregunta 5
    print("Varianza:")
    print(df_p1['emails_phishing'].var())
    print()

    # pregunta 6
    print("Valor maximo:")
    print(df_p1['emails_phishing'].max())
    print()
    print("Valor minimo:")
    print(df_p1['emails_phishing'].min())
    print()

    print("########################################################################")
    print()
    print("CONTRASEÑA DEBIL")

    # pregunta 1
    print("Numero de observaciones de emails phishing: ")
    print(df_pwd_nosec['emails_phishing'].count())
    print()

    # pregunta 2
    print("Numero missings:")
    if df_pwd_nosec['emails_phishing'].min() == 0:
        print(df_pwd_nosec['emails_phishing'].value_counts()[0])
    else:
        print("0")
    print()

    # pregunta 3
    print("Mediana:")
    print(df_pwd_nosec['emails_phishing'].median())
    print()

    # pregunta 4
    print("Media:")
    print(df_pwd_nosec['emails_phishing'].mean())
    print()

    # pregunta 5
    print("Varianza:")
    print(df_pwd_nosec['emails_phishing'].var())
    print()

    # pregunta 6
    print("Valor maximo:")
    print(df_pwd_nosec['emails_phishing'].max())
    print()
    print("Valor minimo:")
    print(df_pwd_nosec['emails_phishing'].min())
    print()

    print("########################################################################")
    print()
    print("CONTRASEÑA SEGURA")

    # pregunta 1
    print("Numero de observaciones de emails phishing: ")
    print(df_pwd_sec['emails_phishing'].count())
    print()

    # pregunta 2
    print("Numero missings:")
    if df_pwd_sec['emails_phishing'].min() == 0:
        print(df_pwd_sec['emails_phishing'].value_counts()[0])
    else:
        print("0")
    print()

    # pregunta 3
    print("Mediana:")
    print(df_pwd_sec['emails_phishing'].median())
    print()

    # pregunta 4
    print("Media:")
    print(df_pwd_sec['emails_phishing'].mean())
    print()

    # pregunta 5
    print("Varianza:")
    print(df_pwd_sec['emails_phishing'].var())
    print()

    # pregunta 6
    print("Valor maximo:")
    print(df_pwd_sec['emails_phishing'].max())
    print()
    print("Valor minimo:")
    print(df_pwd_sec['emails_phishing'].min())


ejercicio3()
