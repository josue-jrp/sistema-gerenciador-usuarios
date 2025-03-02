import os
caminho = os.getcwd() + r"\data-base\bd_passwd.txt"

def gerar():
    with open(fr"{caminho}", "r", encoding="utf-8")as arquivo:
        conteudo = arquivo.readlines()

        ids = [item for item in conteudo if "id = " in item]
        ultimo_id = ids[-1]
        print("esse é o ultimo ID detectado: ", ultimo_id)

        valor_numerico = ultimo_id[4:]
        print("detectando valor numérico: ", valor_numerico)

        proximo_id = int(valor_numerico) + 1
        print("o proximo id será: ", proximo_id)

        return proximo_id

gerar()