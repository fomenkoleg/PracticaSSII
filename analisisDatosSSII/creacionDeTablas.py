import sqlite3
import json
import hashlib as hash
import time


# crear tablas de bbdd
# lectura json
# pasar a bbdd
# leer de bd
# hacer calculos y hacer dataframe y etc,




# Tablas
# usuarios - id username
#   lo explicado
#   campo seguridad de contraseña
#
# IPs - id autoincrement
#       usuario string
#       ip string
#       fecha datetime

def if_secure(password, hashes):
    for h in hashes:
        if password==h:
            print("CONTRASEÑA NO SEGURA ENCONTRADA! la contraseña es: " + password)
            return 0
    return 1
def crear_tabla_users():

    # creamos array de hashes
    hashes = []
    palabras = open('palabras_comunes.txt', 'r')
    for palabra in palabras:

        hash_pass = hash.md5(palabra[:-1].encode(encoding="utf-8")).hexdigest()
        hashes.append(hash_pass)
    print(hashes)

    conn_users = sqlite3.connect('users_data_online.db')
    cursor_user = conn_users.cursor()
    cursor_user.execute("DROP TABLE IF EXISTS user_data_online;")
    cursor_user.execute("""
                    
                    CREATE TABLE IF NOT EXISTS user_data_online(
                    username TEXT PRIMARY KEY,
                    tel_num INTEGER,
                    hash_password TEXT NOT NULL,
                    pass_complexity INTEGER NOT NULL,
                    province TEXT,
                    permisos INTEGER,
                    emails_total INTEGER,
                    emails_phishing INTEGER,
                    emails_clicados INTEGER
                    );
                   """)
    cursor_user.execute("DROP TABLE IF EXISTS users_ips_fechas;")
    cursor_user.execute("""
                        CREATE TABLE IF NOT EXISTS users_ips_fechas(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username_access TEXT NOT NULL,
                        ip_address TEXT,
                        fecha DATETIME,
                        foreign key (username_access) REFERENCES user_data_online(username)
                        );
                       """)
    # aquí apertura del json
    ficheroUsuarios = open('datos/users_data_online.json', 'r')
    datos_usuario = json.load(ficheroUsuarios)


    keys = []
    for i in range(len(datos_usuario['usuarios'])):
        for key in datos_usuario['usuarios'][i]:
            keys.append(key)
    print(keys)

    cont = 0
    for username in keys:
        name = username
        telf = datos_usuario['usuarios'][cont][username]["telefono"]
        if not telf:
            telf = "null"
        password = str(datos_usuario['usuarios'][cont][username]["contrasena"])
        complexity = if_secure(password, hashes)

        province = datos_usuario['usuarios'][cont][username]["provincia"]
        if not province:
            province = "null"
        permisos = int(datos_usuario['usuarios'][cont][username]["permisos"])
        emailsTotal = int(datos_usuario['usuarios'][cont][username]["emails"]["total"])
        emailsPhish = int(datos_usuario['usuarios'][cont][username]["emails"]["phishing"])
        emailsCiclados = int(datos_usuario['usuarios'][cont][username]["emails"]["cliclados"])


        # por iterar
        fechas = datos_usuario['usuarios'][cont][username]["fechas"]
        ips = datos_usuario['usuarios'][cont][username]["ips"]
        cont += 1

        cursor_user.execute(f"""
                            INSERT INTO user_data_online(
                            username, tel_num, hash_password, pass_complexity, province, permisos, emails_total, emails_phishing, emails_clicados)
                            VALUES ('{name}', '{telf}', '{password}', '{complexity}', '{province}', '{permisos}', '{emailsTotal}', '{emailsPhish}', '{emailsCiclados}')
                            """)
        conn_users.commit()

        # iteramos por las IPs y fechas
        for i in range(len(ips)):
            ip = str(ips[i])
            fech = str(fechas[i])
            cursor_user.execute(f"""
                        INSERT INTO users_ips_fechas(
                        username_access, ip_address, fecha)
                        VALUES ('{username}', '{ip}', '{fech}');
            """)
            conn_users.commit()

    #test = cursor_user.execute("SELECT pass_complexity FROM user_data_online;")
    #print(test.fetchall())
    conn_users.close()

def crear_tabla_legal():
    conn_users = sqlite3.connect('users_data_online.db')
    cursor_user = conn_users.cursor()
    cursor_user.execute("DROP TABLE IF EXISTS legal_data_online;")
    cursor_user.execute("""

                        CREATE TABLE IF NOT EXISTS legal_data_online(
                        web TEXT PRIMARY KEY,
                        cookies INTEGER NOT NULL,
                        aviso INTEGER NOT NULL,
                        proteccion INTEGER NOT NULL,
                        creacion INTEGER NOT NULL
                        );
                       """)
    # aquí apertura del json
    ficheroLegal = open('datos/legal_data_online.json', 'r')
    legal_datos = json.load(ficheroLegal)

    keys = []
    for i in range(len(legal_datos['legal'])):
        for key in legal_datos['legal'][i]:
            keys.append(key)
    

    cont = 0
    for web in keys:
        web = str(web)
        cookies = str(legal_datos['legal'][cont][web]['cookies'])
        aviso = str(legal_datos['legal'][cont][web]['aviso'])
        proteccion_de_datos = str(legal_datos['legal'][cont][web]['proteccion_de_datos'])
        creacion = str(legal_datos['legal'][cont][web]['creacion'])

        cont += 1

        cursor_user.execute(f"""
                                    INSERT INTO legal_data_online(
                                    web, cookies, aviso, proteccion, creacion)
                                    VALUES ('{web}', '{cookies}', '{aviso}', '{proteccion_de_datos}', '{creacion}')
                                    """)
        conn_users.commit()


    conn_users.close()


crear_tabla_users()
crear_tabla_legal()
