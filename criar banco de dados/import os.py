import os
import shutil

def criar_diretorios(diretorios):
    """
    Cria os diretórios especificados na lista 'diretorios' caso não existam.
    
    Args:
        diretorios (list): Lista de caminhos de diretórios a serem criados.
    """
    for diretorio in diretorios:
        # Verifica se o diretório já existe
        if not os.path.exists(diretorio):
            try:
                # Tenta criar o diretório e suas subpastas
                os.makedirs(diretorio)
                print(f"Diretório {diretorio} criado.")
            except PermissionError:
                # Captura erro de permissão caso o diretório não possa ser criado
                print(f"Sem permissão para criar o diretório {diretorio}.")
            except Exception as e:
                # Captura qualquer outro erro inesperado
                print(f"Erro inesperado ao criar {diretorio}: {e}")

def mover_arquivos(diretorio_origem):
    """
    Move arquivos com extensões específicas ('pdf', 'txt', 'jpg') para seus respectivos diretórios.
    
    Args:
        diretorio_origem (str): Caminho do diretório onde os arquivos estão atualmente.
    """
    # Lista todos os arquivos no diretório de origem
    for arquivo in os.listdir(diretorio_origem):
        caminho_arquivo = os.path.join(diretorio_origem, arquivo)
        
        # Verifica se o caminho corresponde a um arquivo regular
        if os.path.isfile(caminho_arquivo):
            # Obtém a extensão do arquivo em minúsculas
            extensao = arquivo.split('.')[-1].lower()
            
            # Verifica se a extensão está na lista de extensões suportadas
            if extensao in ['pdf', 'txt', 'jpg']:
                # Define o diretório de destino com base na extensão
                diretorio_destino = os.path.join(diretorio_origem, extensao)
                try:
                    # Move o arquivo para o diretório de destino
                    shutil.move(caminho_arquivo, diretorio_destino)
                    print(f"{arquivo} movido para {diretorio_destino}.")
                except PermissionError:
                    # Captura erro de permissão caso o arquivo não possa ser movido
                    print(f"Sem permissão para mover {arquivo}.")
                except Exception as e:
                    # Captura qualquer outro erro inesperado
                    print(f"Erro inesperado ao mover {arquivo}: {e}")
                else:
                    # Este bloco 'else' é executado se nenhuma exceção ocorrer
                    # Porém, parece haver um erro lógico aqui, pois a mensagem indica que a extensão não é suportada
                    print(f"Extensão {extensao} de {arquivo} não é suportada.")

def main():
    """
    Função principal que define o diretório de trabalho, cria os diretórios necessários
    e move os arquivos para seus respectivos diretórios.
    """
    # Define o diretório de trabalho
    diretorio_trabalho = "diretorio_trabalho"
    
    # Lista dos diretórios a serem criados dentro do diretório de trabalho
    diretorios = [
        os.path.join(diretorio_trabalho, 'pdf'),
        os.path.join(diretorio_trabalho, 'txt'),
        os.path.join(diretorio_trabalho, 'jpg')
    ]
    
    # Cria os diretórios se eles não existirem
    criar_diretorios(diretorios)
    
    # Move os arquivos para os diretórios correspondentes com base na extensão
    mover_arquivos(diretorio_trabalho)

if __name__ == "__main__":
    # Executa a função principal quando o script é executado diretamente
    main()
