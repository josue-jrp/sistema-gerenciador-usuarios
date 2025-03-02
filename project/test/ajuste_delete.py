import os

caminho = os.getcwd()
caminho = caminho + r"\data-base\bd_passwd.txt"

with open(caminho, "r", encoding="utf-8")as file:
    content = file.read()
    print(content)
    new_content = content.replace("\n", "@")
    #print("valor de 'new_content' antes do ajuste: ", new_content)
    for i in range(3):
        for indice, letra in enumerate(new_content):
            if letra == "-":
                print(f"traço encontrado! indice {indice}")

                if new_content[indice - 1] == "-" or new_content[indice - 2] == "-" or new_content[indice - 3] == "-" or new_content[indice - 4] == "-":
                    print("duplicidade de traços encontrada!")
                    lista = list(new_content)
                    lista[indice] = ""
                    new_content = "".join(lista)
                    new_content.strip()
                    #print("conteudo atualizado: ", new_content)

                    format_content = ''

                    for indice, item in enumerate(new_content):
                        if "@" == item:
                            format_content = new_content.replace("@", "\n")

                    print("format_content:\n" , format_content.strip())


                    with open(caminho, "w", encoding="utf-8")as file:
                        file.write(format_content)
                        print("arquivo corrigido!")

    else:
        print("nenhuma duplicidade de traços encontrada no documento!")
    