import os
import duplicity_checker as dc

def id_generator(content):
    try:
        # reconhecimento de valores de ID para possível criação de novo ID
                intervalo = list(range(0, 100))
                index_search = list()
                for indice, item in enumerate(content):
                    for valor in intervalo:
                        valor = str(valor)
                        if f"id = {valor}" in item:
                            index_search.append(content[indice])               
                last_value = index_search[-1]
                list_last_value = list(last_value)
                for indice , item in enumerate(list_last_value):
                    response = item.isnumeric()
                    if response: 
                        format_last_value = list_last_value[indice]
                # encontrando qual é o próximo indice
                id = int(format_last_value) + 1
                return True, f"id = {id}"
    except TypeError as error:
        print("o erro ocorreu no arquivo 'create_user', na função 'id_generator'\n")
        print("tipo de erro: ", error)

def create_user(username, passwd, re_passwd):

    try:
        if passwd != re_passwd:
            print("\n[ERRO]\nas senhas fornecidas não são iguais\n")
            return False
        elif len(passwd) == 0:
            print("\n[ERRO]\ndigite corretamente\n") 
            return False
        
        else:
            caminho = os.getcwd()
            with open(fr"{caminho}\data-base\bd_passwd.txt", "r+", encoding="utf-8")as arquivo:
                content = arquivo.readlines()

                #chamada de função que gera novo ID
                response, id = id_generator(content) # esss 'id' abaixo vem pronto no formato que é para 'escrever' no arquivo 'bd_passwd.txt'
                if "-" in content[-1] or "-\n" in content[-1]:
                    new_user = f"{id}\nusername = {username}\npasswd = {passwd}\n-\n"

                else:
                    new_user = f"\n-\n{id}\nusername = {username}\npasswd = {passwd}\n-\n"

                possibility = dc.duplicity_checker(username, content) 

                if possibility:
                    return new_user
                
                else:
                    print("\nesse username já está cadastrado!")
                    return False
            
    except TypeError as error:
        print("[erro] " , error)
