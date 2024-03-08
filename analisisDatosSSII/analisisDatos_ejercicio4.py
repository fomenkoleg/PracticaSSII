import sqlite3
import pandas
import matplotlib.pyplot as plt
import pandas as pd

conn = sqlite3.connect('users_data_online.db')


# parte 1

query_ips_normal = "SELECT * FROM users_ips_fechas WHERE username_access IN (SELECT username FROM user_data_online  WHERE permisos IS 0);"
query_ips_admin = "SELECT * FROM users_ips_fechas WHERE username_access IN (SELECT username FROM user_data_online  WHERE permisos IS 1);"
df_ips_normal = pd.read_sql_query(query_ips_normal, conn)
df_ips_admin = pd.read_sql_query(query_ips_admin, conn)

df_ips_normal = pd.to_datetime(df_ips_normal['fecha'], format="%d/%m/%Y")
df_ips_admin = pd.to_datetime(df_ips_admin['fecha'], format="%d/%m/%Y")

df_ips_normal = df_ips_normal.sort_values('fecha')
df_ips_admin = df_ips_admin.sort_values('fecha')

print(df_ips_normal)
print()
print(df_ips_admin)

