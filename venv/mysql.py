import pymysql

con = pymysql.connect("localhost", "root", "")
cursor = con.cursor()
bd = "quartoanoinfo"
cursor.execute("CREATE DATABASE "+bd)

try:
    cursor.execute(sql)
    print("Banco conectado")
    con.commit()
except:
    print("Erro !")
    con.rollback()

