"""
import os

for item in os.listdir(os.getcwd()):
    if os.path.isfile(item):
        print(item)
    else:
        print(item)
"""
"""
def autentication_login(usr, passwd):
    with open("C:\\Users\\josue\\OneDrive\\Documentos\\vscode-python\\python-projects\\projeto-gestor-tarefas2\\project\\bd_passwd.txt", "r", encoding="utf-8")as bd_senhas:
        username = bd_senhas.readlines()

        for valor in username:
            if "\n" in valor:
                b_valor = valor.replace("\n", "")
                valor_antigo = username.index(valor)
                username[valor_antigo] = b_valor

        #formatando banco de dados para conseguir manipular e consultar
        print(username)
        concatenado = " ".join(username)
        print(concatenado)
        separador = concatenado.split(" - ")

        for valor in separador:
            valor = valor.strip()
            print(valor)

        print(separador)

        #de fato, o login
        for valor in separador:
            if valor == f"username = {usr} passwd = {passwd}":
                return "login autorizado"
        
        return "login não autorizado"

nome = input("Digite o nome: ")
senha = input("Digite a senha: ")

res = autentication_login(nome, senha)

print(res)
"""

"""
import os
import time
import shutil

caminho = r"C:\Users\josue\OneDrive\Documentos\vscode-python\python-projects\projeto-gestor-tarefas2\project\data-base"
caminho_users = r"C:\Users\josue\OneDrive\Documentos\vscode-python\python-projects\projeto-gestor-tarefas2\project\data-base\credentials_users"

if os.path.exists(caminho):
    print("o diretório [data-base] já existe.")
    time.sleep(1)
    print("verificando se [credentials_users] já existe.")
    time.sleep(1)
    if os.path.exists(caminho_users):
        print("o diretório [credentials_users] já existe.")
    else:
        print("o diretório não existe.")
        time.sleep(1)
        print("criando diretório [credentials_users] dentro de [data-base]")
        for i in range(4):
            print("#"*i)
            time.sleep(1)
        os.makedirs(caminho_users)

        if os.path.exists(caminho_users):
            print("Diretório criado com sucesso.")
else:
    print("o diretório não existe.")
    os.makedirs(f"{caminho}")
    print("Diretório criado.")
"""
