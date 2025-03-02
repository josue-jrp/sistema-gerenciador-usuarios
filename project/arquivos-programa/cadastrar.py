import os
caminho = os.getcwd()
import gerador_id

def checagem_duplicidade(chave_entrada):

    with open(caminho + r"\data-base\bd_passwd.txt", "r", encoding="utf-8")as arquivo:
        conteudo = arquivo.readlines()
        conteudo = [item for item in conteudo if item != "\n"]
        conteudo_f = [item.replace("\n", "") for item in conteudo]
        print(fr"conteudo formatado: {conteudo_f}")
        for item in conteudo_f:
            if item == chave_entrada:
                print("o usuário já está cadastrado no sistema!")
                return False, ""
        else:
            return True, conteudo
            
        # após o processo anterior, agora é o momento de adicionar uma funcionalidade ao código chamado checagem de duplicidade
        # esta funcionalidade existe para checar se não há outro usuário com o mesmo nome no banco de dados

def cadastrar(nome, senha):
    if " " in nome:
        nome = nome.replace(" ", "_")
        
    print(fr"nome obtido: {nome} - senha obtida: {senha}")
    print("deu certo até aqui!")
    chave = f"username = {nome.strip()}" #essa 'chave' vai ser passada para ser comparada com cada item dentro do documento. Se algum item for identico a chave, significa que o usuário já está cadastrado.
    resposta, conteudo = checagem_duplicidade(chave)

    if resposta:
        print("o usuário não está cadastrado no sistema!")
        id = gerador_id.gerar()
        credenciais_usuario = f"id = {id}\nusername = {nome}\npasswd = {senha}\n-\n"
        conteudo.append(credenciais_usuario)

        with open(fr"{caminho}\data-base\bd_passwd.txt", "w", encoding="utf-8")as arquivo:
                
            arquivo.writelines(conteudo)
            
            return True
    
    else:
        print("O usuário já está cadastrado no sitema!")
        return False