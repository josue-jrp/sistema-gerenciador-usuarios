import os

caminho = os.getcwd()

caminho = caminho + r"\test\arquivo_teste.txt"

with open(fr"{caminho}", "r", encoding="utf-8")as file:
    content = file.readlines()
    linhas = [linha for linha in content if linha != "\n"]

    print(len(linhas))

with open(fr"{caminho}", "w", encoding="utf-8")as file:
    for item in linhas:
        file.write(item)