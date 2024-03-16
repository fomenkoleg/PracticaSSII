import pandas as pd
import sqlite3

def ejercicio3():
    answer = ''
    # Conectamos con la base de datos
    conn = sqlite3.connect('users_data_online.db')

    # Hacemos las consultas para obtener los ususarios con permiso 0 o 1 respectivamente
    query_permisos_0 = "SELECT * FROM user_data_online WHERE permisos=0"
    query_permisos_1 = "SELECT * FROM user_data_online WHERE permisos=1"

    # Y se crean los correspondientes DataFrames
    df_p0 = pd.read_sql_query(query_permisos_0, conn)
    df_p1 = pd.read_sql_query(query_permisos_1, conn)

    # Lo mismo para las contraseñas seguras e inseguras
    query_pass_sec = "SELECT * FROM user_data_online WHERE pass_complexity=true"
    query_pass_noSec = "SELECT * FROM user_data_online WHERE pass_complexity=false"

    df_pwd_sec = pd.read_sql_query(query_pass_sec, conn)
    df_pwd_nosec = pd.read_sql_query(query_pass_noSec, conn)

    answer += ("PERMISOS DE USUARIO") + '\n'

    # pregunta 1
    answer += ("Numero de observaciones de emails phishing: ") + '\n'
    answer += str(df_p0['emails_phishing'].count()) + '\n'
    answer +=   '\n'

    # pregunta 2
    answer += ("Numero missings:") + '\n'
    if df_p0['emails_phishing'].min() == 0:
        answer += str(df_p0['emails_phishing'].value_counts()[0]) + '\n'
    else:
        answer += ("0") + '\n'
    answer +=  '\n'

    # pregunta 3
    answer += ("Mediana:") + '\n'
    answer += str(df_p0['emails_phishing'].median()) + '\n'
    answer +=   '\n'

    # pregunta 4
    answer += ("Media:") + '\n'
    answer += str(df_p0['emails_phishing'].mean()) + '\n'
    answer +=  '\n'

    # pregunta 5
    answer += ("Varianza:") + '\n'
    answer += str(df_p0['emails_phishing'].var()) + '\n'
    answer +=   '\n'

    # pregunta 6
    answer += ("Valor maximo:") + '\n'
    answer += str(df_p0['emails_phishing'].max()) + '\n'
    answer +=  '\n'
    answer += ("Valor minimo:") + '\n'
    answer += str(df_p0['emails_phishing'].min()) + '\n'
    answer +=   '\n'

    answer += ("########################################################################") + '\n'
    answer +=  '\n'
    answer += ("PERMISOS DE ADMIN") + '\n'

    # pregunta 1
    answer += ("Numero de observaciones de emails phishing: ") + '\n'
    answer += str(df_p1['emails_phishing'].count()) + '\n'
    answer +=   '\n'

    # pregunta 2
    answer += ("Numero missings:") + '\n'
    if df_p1['emails_phishing'].min() == 0:
        answer += str(df_p1['emails_phishing'].value_counts()[0]) + '\n'
    else:
        answer += ("0") + '\n'
    answer +=  '\n'

    # pregunta 3
    answer += ("Mediana:") + '\n'
    answer += str(df_p1['emails_phishing'].median()) + '\n'
    answer +=  '\n'

    # pregunta 4
    answer += ("Media:") + '\n'
    answer += str(df_p1['emails_phishing'].mean()) + '\n'
    answer +=  '\n'

    # pregunta 5
    answer += ("Varianza:") + '\n'
    answer += str(df_p1['emails_phishing'].var()) + '\n'
    answer +=  '\n'

    # pregunta 6
    answer += ("Valor maximo:") + '\n'
    answer += str(df_p1['emails_phishing'].max()) + '\n'
    answer +=  '\n'
    answer += ("Valor minimo:") + '\n'
    answer +=str(df_p1['emails_phishing'].min()) + '\n'
    answer +=   '\n'

    answer += ("########################################################################") + '\n'
    answer +=  '\n'
    answer += ("CONTRASEÑA DEBIL") + '\n'

    # pregunta 1
    answer += ("Numero de observaciones de emails phishing: ") + '\n'
    answer += str(df_pwd_nosec['emails_phishing'].count()) + '\n'
    answer +=  '\n'

    # pregunta 2
    answer += ("Numero missings:") + '\n'
    if df_pwd_nosec['emails_phishing'].min() == 0:
        answer += str(df_pwd_nosec['emails_phishing'].value_counts()[0]) + '\n'
    else:
        answer += ("0") + '\n'
    answer += '\n'

    # pregunta 3
    answer += ("Mediana:") + '\n'
    answer += str(df_pwd_nosec['emails_phishing'].median()) + '\n'
    answer +=  '\n'

    # pregunta 4
    answer += ("Media:") + '\n'
    answer += str(df_pwd_nosec['emails_phishing'].mean()) + '\n'
    answer +=  '\n'

    # pregunta 5
    answer += ("Varianza:") + '\n'
    answer += str(df_pwd_nosec['emails_phishing'].var()) + '\n'
    answer += '\n'

    # pregunta 6
    answer += ("Valor maximo:") + '\n'
    answer += str(df_pwd_nosec['emails_phishing'].max()) + '\n'
    answer += '\n'
    answer += ("Valor minimo:") + '\n'
    answer += str(df_pwd_nosec['emails_phishing'].min()) + '\n'
    answer +=  '\n'

    answer += ("########################################################################") + '\n'
    answer += '\n'
    answer += ("CONTRASEÑA SEGURA") + '\n'

    # pregunta 1
    answer += ("Numero de observaciones de emails phishing: ") + '\n'
    answer += str(df_pwd_sec['emails_phishing'].count()) + '\n'
    answer += '\n'

    # pregunta 2
    answer += ("Numero missings:") + '\n'
    if df_pwd_sec['emails_phishing'].min() == 0:
        answer += str(df_pwd_sec['emails_phishing'].value_counts()[0]) + '\n'
    else:
        answer += ("0") + '\n'
    answer += '\n'

    # pregunta 3
    answer += ("Mediana:") + '\n'
    answer += str(df_pwd_sec['emails_phishing'].median()) + '\n'
    answer += '\n'

    # pregunta 4
    answer += ("Media:") + '\n'
    answer += str(df_pwd_sec['emails_phishing'].mean()) + '\n'
    answer +=  '\n'

    # pregunta 5
    answer += ("Varianza:") + '\n'
    answer += str(df_pwd_sec['emails_phishing'].var()) + '\n'
    answer += '\n'

    # pregunta 6
    answer += ("Valor maximo:") + '\n'
    answer += str(df_pwd_sec['emails_phishing'].max()) + '\n'
    answer += '\n'
    answer += ("Valor minimo:") + '\n'
    answer += str(df_pwd_sec['emails_phishing'].min()) + '\n'

    return answer
ejercicio3()
