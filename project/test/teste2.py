import os

def create_user(username, passwd):
    with open("arquivo_teste.txt", "r+", encoding="utf-8")as arquivo:
        data_file = arquivo.readlines()
        print(data_file)
        # formating_data_file
        #f_data_file = "".join(fr"{data_file}")
        for indice, item in enumerate(data_file):
            if "\n" in item:
                data_file[indice] = item.replace("\n", "")

        f_data_file = " ".join(data_file)
        print(data_file)
        print(f_data_file)
        f_data_file = f_data_file.split(" - ")
        print(f_data_file)
    
        for indice, item in enumerate(f_data_file):
            if " = " in item:
                f_data_file[indice] = item.replace(" = ", "@")
        
        print(f_data_file)

        print("\nINFORMAÇÃO DE 'BD_PASSWD': \n")
        print("todos os username: ")
        format_user_passwd = []
        for item in f_data_file:
            indice_arroba = item.find("@")
            indice_space = item.find(" ")
            print("usuário: ", item[indice_arroba+1:indice_space] )

            v_contadora = 0
            
            for indice, letra in enumerate(item):
                if "@" == letra:
                    v_contadora += 1
                    if v_contadora == 2:
                        list_item = list(item)
                        list_item[indice] = letra.replace("@", "#")
                        format_item = "".join(list_item)
                        format_user_passwd.append(format_item)
                        v_contadora = 0
        print("\nTodos os pares username - password: ")
        for item in format_user_passwd:
            print(item)            
        print("")

        #após ver se é possivel criar o usuário, se possível, é atribuído um ID ao usuário novo e incluido junto do seu registro no "banco de dados"
        id = "x"
    
    # -- ------- -- -- -- - -- - -- - -  -

    with open("arquivo_teste.txt", "a+", encoding="utf-8")as arquivo:
        arquivo.seek(2)
        arquivo.write("\n-")
        arquivo.write("\nid = " + id)
        arquivo.write("\nusername = " + username)
        arquivo.write("\npasswd = " + passwd)

        return True, id

"""
username = input("Digite o seu username: ")
passwd = input("Digite a sua senha: ")
confirm_passwd = input("Confirme a sua senha: ")
"""

username = input("nome de usuário: ")
passwd = input("Senha: ")
re_passwd = input("Repita a senha: ")

if username == " " or passwd == " " or len(username) == 0 or len(passwd) == 0:
    print("Erro ao criar um novo usuário [digitou incorretamente] ")
else:
    if passwd != re_passwd:
        print("erro ao criar um novo usuário [a confirmação de senha está diferente]")
    else:
        response = create_user(username, passwd)
        if response:
            print("usuário criado com sucesso [sucesso]")