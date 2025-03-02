import os
arquivo = os.getcwd() + r"\data-base\bd_passwd.txt"

def verificar_credenciais(nome, senha):
    nome = nome.strip()
    senha = senha.strip()

    if " " in nome:
        nome = nome.replace(" ", "_")

    username = fr"username = {nome}"
    passwd = fr"passwd = {senha}"

    with open(arquivo, "r", encoding="utf-8")as file:
        conteudo = file.readlines()
        conteudo_f = [item.replace("\n", "") for item in conteudo if item != "\n"]
        print(conteudo_f)

        indice_username = 0

        for indice, valor in enumerate(conteudo_f):
            if username == valor:
                print("username fornecido está no BD.")
                indice_username = indice
                break
        
        if conteudo_f[indice_username + 1] == passwd:
            print("usuário autenticado com sucesso!")
            return True, fr"login feito por [{conteudo_f[indice_username -1]} {conteudo_f[indice_username]} {conteudo_f[indice_username + 1]}]"

        else:
            print("usuário ou senha incorreta!")
            return False, "usuário ou senha incorreta!"
        
    