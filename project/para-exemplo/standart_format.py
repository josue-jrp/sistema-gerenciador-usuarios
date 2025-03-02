# essa função é responsável por pegar os dados alterados sem o padrão de formatação que é exigido em documentos e formata-los

# ela deve fornecer suporte para diversas alterações (deleter usuário, adicionar usuário, visualizar usuário, etc)

# os dados que essa função vai receber como parametros devem ser padronizados no formato de listas (abaixo):
# ['id = 0','username = exemple','passwd = example','-'] 

def format(conteudo):
    conteudo_f = []

    for item in conteudo:
        lista = list(item)
        lista.append("\n")
        conteudo_f.append("".join(lista))

    return conteudo_f