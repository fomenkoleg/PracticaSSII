import sqlite3
import matplotlib.pyplot as plt
import pandas as pd


def ejercicio4_1():

    conn = sqlite3.connect('users_data_online.db')
    # parte 1

    query_ips_normal = "SELECT * FROM users_ips_fechas WHERE username_access IN (SELECT username FROM user_data_online  WHERE permisos IS 0);"
    query_ips_admin = "SELECT * FROM users_ips_fechas WHERE username_access IN (SELECT username FROM user_data_online  WHERE permisos IS 1);"
    df_ips_normal = pd.read_sql_query(query_ips_normal, conn)
    df_ips_admin = pd.read_sql_query(query_ips_admin, conn)

    df_ips_normal['fecha'] = pd.to_datetime(df_ips_normal['fecha'], format="%d/%m/%Y")
    df_ips_admin['fecha'] = pd.to_datetime(df_ips_admin['fecha'], format="%d/%m/%Y")

    df_ips_normal = df_ips_normal.sort_values(by=['username_access', 'fecha'])
    df_ips_admin = df_ips_admin.sort_values(by=['username_access', 'fecha'])

    df_ips_normal['diferencia'] = pd.to_numeric(df_ips_normal.groupby('username_access')['fecha'].diff().dt.days)
    df_ips_admin['diferencia'] = pd.to_numeric(df_ips_admin.groupby('username_access')['fecha'].diff().dt.days)


    print("La media de tiempo medio entre cambios de contraseña por usuario normal (en días): ")
    medias_ips_normal = df_ips_normal.groupby('username_access')['diferencia'].mean()
    medias_ips_normal['tiempo_medio'] = df_ips_normal['diferencia']
    medias_ips_normal.drop(['diferencia'])
    print(medias_ips_normal)

    print("La media de tiempo medio entre cambios de contraseña por usuario administrador (en días): ")
    medias_ips_admin = df_ips_admin.groupby('username_access')['diferencia'].mean()
    medias_ips_admin['tiempo_medio'] = df_ips_admin['diferencia']
    medias_ips_admin.drop(['diferencia'])
    print(medias_ips_admin)

    plt.figure(figsize=(25, 16))

    plt.subplot(1, 2, 1)
    plt.title('Tiempo medio trascurrido en días ara usuarios normales')
    medias_ips_normal.plot(kind='bar', x='username_access', y='', color='aqua')

    plt.subplot(1, 2, 2)
    plt.title('Tiempo medio trascurrido en días ara usuarios admin')
    medias_ips_admin.plot(kind='bar', x='username_access', y='Tiempo medio trascurrido', color='magenta')

    plt.show()
def ejercicio4_2():
    conn = sqlite3.connect('users_data_online.db')
    query_inseguros = 'SELECT username, emails_clicados, emails_phishing FROM user_data_online WHERE pass_complexity IS 0 AND emails_clicados IS NOT "None" AND emails_phishing IS NOT "None";'
    df_inseguros = pd.read_sql_query(query_inseguros, conn)
    df_inseguros['probabilidad_phishing'] = (df_inseguros['emails_clicados']/df_inseguros['emails_phishing'])*100

    df_inseguros.sort_values(by=['probabilidad_phishing'])
    df_inseguros.drop(['emails_clicados', 'emails_phishing'], axis=1, inplace=True)
    print(df_inseguros)
    df_inseguros = df_inseguros.head(10)

    df_inseguros.plot(kind='bar', color='aqua')
    plt.title("Probabilidad de éxito de ataque de phishing")
    plt.xlabel("Usuario")
    plt.ylabel("Probabilidad de éxito")
    plt.legend()
    plt.tight_layout()
    plt.show()
def ejercicio4_3():

    conn = sqlite3.connect('users_data_online.db')

    query_webs = 'SELECT web, cookies, aviso, proteccion FROM legal_data_online;'
    df_webs = pd.read_sql_query(query_webs, conn)
    df_webs['desactualizadas'] = df_webs[['cookies', 'aviso', 'proteccion']].apply(lambda row: sum(row == 0), axis=1)
    # para que en la gráfica aparezca con el nombre del sitio web
    df_webs = df_webs.set_index('web')
    print(df_webs)
    df_webs.sort_values(by=['desactualizadas'], inplace=True, ascending=False)
    primeros_cinco = df_webs.head(5)
    primeros_cinco.plot(kind='bar')
    plt.title('Políticas desactualizadas por página web')
    plt.xlabel('Página Web')
    plt.ylabel('Estado')
    plt.legend()

    plt.tight_layout()
    plt.show()
def ejercicio4_4():
    conn = sqlite3.connect('users_data_online.db')
    query_webs = 'SELECT web, creacion, cookies, aviso, proteccion FROM legal_data_online;'

    df_webs = pd.read_sql_query(query_webs, conn)

    df_webs['satisface'] = (df_webs['cookies'] == 1) & (df_webs['aviso'] == 1) & (df_webs['proteccion'] == 1)

    df_webs_agrupado_dos_columnas= df_webs.groupby(['creacion', 'satisface']).size().unstack()
    print(df_webs_agrupado_dos_columnas)

    df_webs_agrupado_dos_columnas.plot(kind='bar')
    plt.title('Webs por año que cumplen las políticas de seguridad')
    plt.xlabel('Año creación')
    plt.ylabel('Número de sitios web')
    plt.legend(['No se cumple', 'Se cumple'])
    plt.tight_layout()
    plt.show()


ejercicio4_1()
ejercicio4_2()
ejercicio4_3()
ejercicio4_4()