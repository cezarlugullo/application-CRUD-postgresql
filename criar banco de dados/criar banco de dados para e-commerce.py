#Objetivo
#Desenvolver um script em Python que:

#Conecte-se a um banco de dados SQLite.
#Crie três tabelas: Produtos, Clientes e Pedidos.
#Insira dados iniciais nessas tabelas.
#Selecione e exiba os dados armazenados.


# Passo 1: Conectar-se ao banco de dados

# No arquivo gerenciamento_ecommerce.py, importe a biblioteca sqlite3.
# Crie uma função para conectar-se ao banco de dados.

import sqlite3

def conectar_banco(nome_banco):
    conexao = sqlite3.connect(nome_banco)
    return conexao

# Passo 2: Criar tabelas

# Defina uma função para criar as tabelas Produtos, Clientes e Pedidos.

def criar_tabelas(conexao):
    cursor = conexao.cursor()
   
    cursor.execute('''CREATE TABLE IF NOT EXISTS Produtos (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      nome TEXT NOT NULL,
                      preco REAL NOT NULL,
                      estoque INTEGER NOT NULL)''')
   
    cursor.execute('''CREATE TABLE IF NOT EXISTS Clientes (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      nome TEXT NOT NULL,
                      email TEXT NOT NULL)''')
   
    cursor.execute('''CREATE TABLE IF NOT EXISTS Pedidos (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      cliente_id INTEGER NOT NULL,
                      produto_id INTEGER NOT NULL,
                      quantidade INTEGER NOT NULL,
                      data_pedido TEXT NOT NULL,
                      FOREIGN KEY (cliente_id) REFERENCES Clientes(id),
                      FOREIGN KEY (produto_id) REFERENCES Produtos(id))''')
   
    conexao.commit()

# Passo 3: Inserir dados iniciais

# Defina uma função para inserir dados nas tabelas.
    
def inserir_dados(conexao):
    cursor = conexao.cursor()
   
    produtos = [('Notebook', 2999.99, 10),
                ('Smartphone', 1999.99, 20),
                ('Tablet', 999.99, 30)]
   
    clientes = [('Alice', 'alice@example.com'),
                ('Bob', 'bob@example.com'),
                ('Charlie', 'charlie@example.com')]
   
    pedidos = [(1, 1, 2, '2023-06-15'),
               (2, 2, 1, '2023-06-16'),
               (3, 3, 3, '2023-06-17')]
   
    cursor.executemany('INSERT INTO Produtos (nome, preco, estoque) VALUES (?, ?, ?)', produtos)
    cursor.executemany('INSERT INTO Clientes (nome, email) VALUES (?, ?)', clientes)
    cursor.executemany('INSERT INTO Pedidos (cliente_id, produto_id, quantidade, data_pedido) VALUES (?, ?, ?, ?)', pedidos)
   
    conexao.commit()

# Passo 4: Montar o script principal

# No final do arquivo gerenciamento_ecommerce.py, adicione o código principal para executar as funções definidas.
    
if __name__ == '__main__':
    conexao = conectar_banco('ecommerce.db')
    criar_tabelas(conexao)
    inserir_dados(conexao)
    conexao.close()