import os

def home(id_user, cont_bd_passwd):
    space = " "
    content = list(cont_bd_passwd)
    v_contadora = 0

    for indice, item in enumerate(content):
        if item == space :
            v_contadora = v_contadora + 1
            if v_contadora == 3:
                content[indice] = ","
                v_contadora = 0

    # Este foi o processo de formatação dos dados do usuário que acabou de logar   
    content_join = "".join(content)    
    content_format = content_join.split(",")
    print("Dados do usuário atual:\n")
    for item in content_format:
        print(item)
    
    def format_id(id):
        lista = list(id)
        for indice, item in enumerate(lista):
            if item == " ":
                lista[indice] = ""

            elif item == "=":
                lista[indice] = "_"

        list_join = "".join(lista)
        return list_join


    id_format = format_id(id_user)