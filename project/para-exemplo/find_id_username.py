def findIdUsername(conteudo):
    retorno = []
    #tirando todos os '\n' dos itens
    for indice, valor in enumerate(conteudo):
        if "\n" in valor:
            conteudo[indice] = conteudo[indice].replace("\n", "")

    #variavel contadora que diz quando não é para o programa mostrar as senhas do usuário  
    c = 0
    print("")
    print("todos os usuários cadastrados no sistema: \n".upper())
    for item in conteudo:
        if "-" in item:
            retorno.append("---\n")
            continue

        else:
            if c == 2:
                c = 0

            else:    
                retorno.append(item)
                c = c +1


    # identificando a resposta do usuário
    return retorno

def findIdUsernamePasswd(conteudo):
    
    retorno = []
    #tirando todos os '\n' dos itens
    for indice, valor in enumerate(conteudo):
        if "\n" in valor:
            conteudo[indice] = conteudo[indice].replace("\n", "")

    #variavel contadora que diz quando não é para o programa mostrar as senhas do usuário  
    c = 0
    print("")
    print("todos os usuários cadastrados no sistema: \n".upper())
    for item in conteudo:
        if "-" in item:
            retorno.append("---\n")
            continue

        else:
            if c == 3:
                c = 0

            else:    
                retorno.append(item)
                c = c +1


    # identificando a resposta do usuário
    return retorno