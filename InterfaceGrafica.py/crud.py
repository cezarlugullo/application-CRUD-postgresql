import psycopg2

class AppBD:
    def __init__(self):
        print('Método Construtor')

    def abrirConexao(self):
        try:
            self.connection = psycopg2.connect(
                user="postgres",
                password="senha123",
                host="127.0.0.1",
                port="5432",
                database="postgres"
            )
            print("Conexão aberta com sucesso!")
        except (Exception, psycopg2.Error) as error:
            print("Falha ao se conectar ao Banco de Dados", error)
            self.connection = None  # Define como None caso a conexão falhe

    # Selecionar todos os Produtos
    def selecionarDados(self):
        registros = []
        try:
            self.abrirConexao()
            if not self.connection:
                print("Conexão não estabelecida.")
                return registros

            cursor = self.connection.cursor()
            sql_select_query = """SELECT * FROM public."PRODUTO" """
            cursor.execute(sql_select_query)
            registros = cursor.fetchall()
            print("Registros selecionados:", registros)

        except (Exception, psycopg2.Error) as error:
            print("Erro na operação de seleção", error)

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")
        
        return registros

    # Inserir Produto
    def inserirDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()
            if not self.connection:
                print("Conexão não estabelecida.")
                return
            
            cursor = self.connection.cursor()
            postgres_insert_query = """INSERT INTO public."PRODUTO" 
            ("CODIGO", "NOME", "PRECO") VALUES (%s,%s,%s) """
            record_to_insert = (codigo, nome, preco)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.connection.commit()
            
            print("Registro inserido com sucesso!")
        
        except (Exception, psycopg2.Error) as error:
            print("Falha ao inserir registro na tabela PRODUTO", error)
        
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")

    # Atualizar Produto
    def atualizarDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()
            if not self.connection:
                print("Conexão não estabelecida.")
                return
            
            cursor = self.connection.cursor()
            sql_update_query = """UPDATE public."PRODUTO" 
                                  SET "NOME" = %s, "PRECO" = %s 
                                  WHERE "CODIGO" = %s"""
            cursor.execute(sql_update_query, (nome, preco, codigo))
            self.connection.commit()
            print("Registro atualizado com sucesso!")

        except (Exception, psycopg2.Error) as error:
            print("Erro na Atualização", error)

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")

    # Excluir Produto
    def excluirDados(self, codigo):
        try:
            self.abrirConexao()
            if not self.connection:
                print("Conexão não estabelecida.")
                return
            
            cursor = self.connection.cursor()
            sql_delete_query = """DELETE FROM public."PRODUTO" WHERE "CODIGO" = %s"""
            cursor.execute(sql_delete_query, (codigo,))
            self.connection.commit()
            print("Registro excluído com sucesso!")
        
        except (Exception, psycopg2.Error) as error:
            print("Erro na Exclusão", error)
        
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")
