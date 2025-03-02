def verificador(itens):
    for item in itens:
        if item == " " or len(item) == 0 or item == "":
            print("campo vazio detectado!")
            return False
    else:
        print("verificação de campos executada. Sem campos vazios!")
        return True