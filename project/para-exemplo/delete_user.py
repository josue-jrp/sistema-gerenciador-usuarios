import os   
import time
import animations
import find_id_username
import standart_format

caminho = os.getcwd()                   

def delete(conteudo_atual, delete_content, target_index):
    
    # conteudo_atual = conteúdo que está no documento txt
    # delete_content = conteúdo que deve ser retirado do documento de texto
    # target_index = indice que foi encontrado o id solicitado pelo usuário

    for i in range(4):
        conteudo_atual[target_index + i] = " "
    
    # tirando os valores em branco da jogada!
    f_conteudo_atual = [valor for valor in conteudo_atual if valor != " " ]

    #print("Isso é o que será retornado para o 'banco de dados'".upper())

    return "[DEL] usuário removido com sucesso", f_conteudo_atual

def intro_delete(): 
    caminho_completo = caminho + r"\data-base\bd_passwd.txt"

    with open(fr"{caminho_completo}", "r", encoding="utf-8")as arquivo:
        content = arquivo.readlines()      
        linhas = [item for item in content if item != "\n"]
        linhas_f = []
        linhas_f = linhas.copy()

        # ids_usernames = conteudo que o usuário pesquisou para saber o que tem no documento
        ids_usernames = find_id_username.findIdUsername(linhas_f)

        # mostrando no console todos os ID e Users que estão cadastrados no 'banco de dados'
        for c in ids_usernames:
            print(c)

        print("\nDigite o ID do user que deseja excluir do 'banco de dados': \n")

        to_delete = input(">")

        user_to_delete = f"id = {to_delete}\n".strip()
    
        # verificando linha por linhas se o id é igual a algum que este no documento, e se for, o script pega somente mais dois valor após o valor do indice e encerra o laço
        target_index = "@"
        for indice, item in enumerate(linhas_f):

            if user_to_delete.strip().lower() == item.strip().lower():
                target_index = int(indice)
                break
        
        if target_index == "@":
            print(f"\n[ERRO] o ID {to_delete} não está cadastrado no sistema!".upper()) 

        else:
            credential_user = []
            for valor in range(4):
                credential_user.append(linhas_f[target_index + valor]) 

            log, retorno = delete(linhas_f, credential_user, target_index)
            #essa 'retorno_f' vai ter os dados atualizados e formatados para somente escrever no 'banco de dados' 
            retorno_f = standart_format.format(retorno)   
            animations.simple_loading()

            with open(fr"{caminho_completo}", "w", encoding="utf-8")as file:
                file.writelines(retorno_f)

            print(f"\nresposta do sistema: {log}") 

def intro():

    while True:
        runner = input("\nDeseja excluir mais algum usuário? (s / n)\n\n>")
        if runner == "s":        
            intro_delete()
        else:
            print("\nVoltando...".upper())
            animations.simple_loading()
            break