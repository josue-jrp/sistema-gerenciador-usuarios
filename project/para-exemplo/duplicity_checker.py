def duplicity_checker(username, content):

    for indice, item in enumerate(content):
        if "\n" in item:
            f_item = item.strip("\n")
            content[indice] = f_item
            
    if f"username = {username}" in content:
        #print("usuário já está cadastrado!")
        return False

    else:
        #print("usuário não está cadastrado!")
        return True