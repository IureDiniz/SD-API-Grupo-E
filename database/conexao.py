import psycopg2

def conectar_bd():
    conexao = psycopg2.connect(
        host="localhost",
        database="banco_academico",
        user="adm",
        password="1234",
        port="5432"
    )

    return conexao

def criar_bd():
    conexao = psycopg2.connect(
            host="localhost",
            database="banco_academico",
            user="adm",
            password="1234",
            port="5432"
        )
    
    cursor = conexao.cursor()

    with open("database/init.sql", "r") as arquivo:
        sql = arquivo.read()
        cursor.execute(sql)
        conexao.commit()

    print("Tabelas criadas com sucesso!")

    cursor.close()
    conexao.close()