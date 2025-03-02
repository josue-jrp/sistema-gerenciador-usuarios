import os
from tkinter import *

arquivo = fr"{os.getcwd()}\data-base\bd_passwd.txt"

def selecionar(id):
    with open(arquivo, "r", encoding="utf-8")as file:
        conteudo = file.readlines()
        conteudo_f = [item for item in conteudo if item != "\n"]
        
        for indice, valor in enumerate(conteudo_f):
            if f"id = {id}\n" == valor:
                print("id encontrado no indice: ", indice)
                credenciais_usuario = conteudo_f[indice:indice+3]
                credenciais_id_username = [item.replace("\n", "") for item in conteudo_f[indice:indice+2]]
                return True, [credenciais_usuario, credenciais_id_username]

        else:
            print("id não foi encontrado!")
            return False, "id não foi encontrado!"
        
def visualizar():
    with open(arquivo, "r", encoding="utf-8")as file:
        conteudo = file.readlines()
        conteudo_f = [item.replace("\n", "") for item in conteudo if item != "\n"]
        ids_usernames = [item for item in conteudo_f if "passwd = " not in item]

        # for para transformar id e username em uma string
        print(ids_usernames)
        ids_usernames_join = " ".join(ids_usernames)
        print(ids_usernames_join)
        ids_usernames = ids_usernames_join.split(" - ")
        print(ids_usernames)

        def arrumar_espacos(lista): # esta função só serve para deixar as coisas mais bonitas e organizadas dentro do listbox de deletar usuários

            for indice, item in enumerate(lista):
                
                if "   " in item and indice < 10:
                    lista[indice] = item.replace("   ", "     ")
            
            return lista

        retorno = [item.replace("id = ", "").replace("username = ", "").replace(" ", "   ").replace("-", "") for item in ids_usernames]

        lista_correcao_espacos = arrumar_espacos(retorno)

        return lista_correcao_espacos

def destruir(widget): # serve para destruir widgets

    widget.destroy()

def deletar_usuario(id_username):
    lista = list(id_username)
    lista[2] = "#"
    print(lista)

    lista_f = [item for item in lista if " " not in item]
    lista_f = "".join(lista_f).lower()
    
    print(lista_f)
    
    indice_de_hashtag = str(lista_f).find("#")
    credenciais_formatadas = f"\nid = {lista_f[:indice_de_hashtag]}\nusername = {lista_f[indice_de_hashtag + 1:]}\n"
    print("credenciais formatadas: ",credenciais_formatadas)

    with open(arquivo, "r", encoding="utf-8")as file:
        conteudo = file.readlines()
        conteudo_join = "".join(conteudo)
        conteudo_user_separado = conteudo_join.split("-")

        print(conteudo_user_separado)

        for indice, item in enumerate(conteudo_user_separado):
            if credenciais_formatadas in item:
                print("usuário encontrado!")
                item_para_excluir = [conteudo_user_separado[indice]]
                item_para_excluir[0] = item_para_excluir[0].replace("\n", "")
                item_para_excluir = str(item_para_excluir[0])
                print(item_para_excluir)

                indice_username = item_para_excluir.find('username')
                id = item_para_excluir[:indice_username]
                print("somente o valor de ID:", fr"{id}\n".strip())

                print("valor de conteudo: ", conteudo)

                for index, valor in enumerate(conteudo):
                    if f"{id}\n" == valor:
                        print("\n\nID encontrado!")
                        print(f"\n\ntodos os valores para excluir: {conteudo[index]}{conteudo[index + 1]}{conteudo[index + 2]} {conteudo[index + 3]}" )

                        # adicionando itens a serem excluídos a uma lista 
                        lista_exclusao = [conteudo[index], conteudo[index + 1], conteudo[index + 2], conteudo[index + 2]]
                        print(lista_exclusao)

                        conteudo_atualizado = conteudo.copy()
                        conteudo_atualizado.pop(index + 3)
                        
                        print(conteudo_atualizado)

                        conteudo_atualizado = [value for value in conteudo_atualizado if value not in lista_exclusao]
                        print("\n\n\n" , conteudo_atualizado)
                        
                        
                        with open(arquivo, "w", encoding="utf-8")as f:
                            f.writelines(conteudo_atualizado)

                            return True 

        else:
            print("usuário não foi encontrado!")
            return False
