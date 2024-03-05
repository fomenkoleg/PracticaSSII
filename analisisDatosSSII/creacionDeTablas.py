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
    if password in hashes:
        print("CONTRASEÑA NO SEGURA ENCONTRADA!")
        return 0
    return 1


def crear_tabla_users():

    # creamos array de hashes
    hashes = []
    palabras = open('palabras_comunes.txt', 'r')
    for palabra in palabras:
        print(palabra)
        hashes.append(hash.md5(palabra.encode()).hexdigest())

    print(len(hashes))



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
        print(password)
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

    test = cursor_user.execute("SELECT hash_password FROM user_data_online;")
    print(test.fetchall())
    conn_users.close()

crear_tabla_users()
#crear_tabla_legal()
