import time
import home
import create_user
import delete_user
import os

caminho = os.getcwd()

def document_corrector():
    #correção do documento
    with open(fr"{caminho}\data-base\bd_passwd.txt", "r+", encoding="utf-8")as file:
        text = file.readlines()
        correction = [item for item in text if item != "\n"]
    
    #aplicando a correção no documento
    with open(fr"{caminho}\data-base\bd_passwd.txt", "w", encoding="utf-8")as file:
        for item in correction:
            file.write(item)

def autentication_login(usr, passwd):
    with open(f"{caminho}\\data-base\\bd_passwd.txt", "r" , encoding="utf-8") as bd_senhas:
        credentials =  bd_senhas.readlines()
        #formatando os dados de login para conseguir manipular e testar com entrada de usuário
        for item in credentials:
            if "\n" in item:
                n_item = item.replace("\n", " ") 
                indice = credentials.index(item)
                credentials[indice] = n_item
                n_item = n_item.strip()
                credentials[indice] = n_item
            str_credentials = " ".join(credentials)
            str_credentials = str_credentials.split(" - ")
        #login, (de fato!)
        chave = f"username = {usr} passwd = {passwd}"
        for valor in str_credentials:
            if valor[7:] == chave:
                #print(f"\no username e password que chaveou é: {valor}")
                print("[login autorizado]")
                id_user = valor[:7]
                return True, id_user, valor
        print("[erro na autenticação]")
        return False, None, None

try:
    while True:
        # função que corrige o documento eliminando toda linha em branco para evitar possiveis erros
        document_corrector()
        print("\n---\nseja bem vindo:\n\n1 - logar\n2 - criar uma conta\n3 - para visualizar contas\n4 - deletar conta\n5 - para outras opções\n")
        res = input("\n>")
        if res == "1":
            while True:
                usr = input("\nusername: ")
                passwd = input("password: ")
                if "exit" in usr or "exit" in passwd:
                    print("\ncancelando operação.")
                    break
                response, id_user, conteudo_bd_passwd = autentication_login(usr, passwd)
                if response:
                    print("\nabrindo a home")
                    for i in range(4):
                        print("#"* i)
                        time.sleep(1)
                    print("home carregada com sucesso!\n")
                    home.home(id_user, conteudo_bd_passwd)
                    break               
                else:
                    break           
        if res == "2":
            print("\n---")
            print("Criação de perfil".upper())
            print("")
            username = input("digite o nome de usuário: ")
            passwd = input("crie uma senha: ")
            re_passwd = input("repita a senha: ")
            response = create_user.create_user(username, passwd, re_passwd)

            if response == False:
                print("\nnão foi possivel cadastrar o usuário no 'banco de dados'! ")

            else:
                for i in range(4):
                    print("#"*i )
                    time.sleep(1)

                with open(fr"{caminho}\data-base\bd_passwd.txt", "a+", encoding="utf-8") as arquivo:
                    arquivo.write(response)
                    print("\nusuário cadastrado com sucesso!\n")

        elif res == "3":
            print("\nAbaixo, será mostrado o 'id' e o 'username' de cada usuário cadastrado\n")
        
        elif res == "4":
            print("você está na área de exclusão de contas, tome cuidado!")
            # função que vai retornar um valor boleano e o novo conteúdo do documento
            delete_user.intro()
            
except TypeError as error:              
    print("\nERRO: ", error)

    