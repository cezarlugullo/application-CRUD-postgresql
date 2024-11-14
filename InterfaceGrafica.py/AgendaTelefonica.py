import psycopg2

try:
    conn = psycopg2.connect(database="postgres", user="postgres", password="senha123", host="127.0.0.1", port="5432")
    print("Conexão com o Banco de Dados aberta com sucesso!")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Agenda (ID INT PRIMARY KEY NOT NULL, Nome TEXT NOT NULL, Telefone CHAR(12));''')
    print("Tabela criada com sucesso!")
    conn.commit()
except psycopg2.OperationalError as e:
    print("Erro ao conectar ao banco de dados:", e)
finally:
    if 'conn' in locals() and conn is not None:
        conn.close()




#Atualização de dados na tabela

import psycopg2
conn = psycopg2.connect(database = " postgres", user="postgres" , password="senha123" , host="127.0.0.1" , port="5432" ) 
print ("Conexão com o Banco de Dados aberta com sucesso!") 
cur=conn.cursor() 
print("Consulta antes da atualização") 
cur.execute("""select * from public."AGENDA" where "id"=1""") 
registro=cur.fetchone() 
print(registro) 
#Atualização de um único registro 
cur.execute("""Update public."AGENDA" set "telefone"='02188888888' where "id"=1""") 
conn.commit() 
print("Registro Atualizado com sucesso! ")
cur = conn.cursor()
print(" Consulta depois da atualização") 
cur.execute("""select * from public."AGENDA" where "id"=1""") 
registro=cur.fetchone() 
print(registro) 
conn.commit() 
print("Seleção realizada com sucesso!");
conn.close()


#Exclusão de dados na tabela

import psycopg2
conn = psycopg2.connect(database = " postgres", user="postgres" , password="senha123" , host="127.0.0.1" , port="5432" ) 
print ("Conexão com o Banco de Dados aberta com sucesso!") 
cur=conn.cursor() 
cur.execute("""Delete from public."AGENDA" where "id"=1""") 
conn.commit() 
cont=cur.rowcount 
print(cont, "Registro excluído com sucesso!") 
print("Exclusão realizada com sucesso!"); 
conn.close()


#Geração de dados aleatórios

from faker import Faker
import psycopg2

conn = psycopg2.connect(database = "postgres", user = "postgres",
                        password = "senha123", host = "127.0.0.1", port = "5432")
print ("Conexão aberta com sucesso!")
cursor = conn.cursor()
fake = Faker ('pt_BR')

n=10
for i in range(n):
    codigo = i+10
    nome = 'produto_' + str(i+1)
    preco = fake.pyfloat(left_digits=3,right_digits=2, positive=True,
                         min_value=5,max_value=1000)
    print(preco)
    print(nome)

    comandoSQL = """ INSERT INTO public."PRODUTO" ("CODIGO", "NOME", "PRECO")
    VALUES (%s, %s, %s) """
    registro = (codigo, nome, preco)
    cursor.execute(comandoSQL, registro)

conn.commit()
print("Inserção realizada com sucesso!");
conn.close()