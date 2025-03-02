from tkinter import *
from tkinter.ttk import Progressbar
import cadastrar
import verificador_campos_vazios # lembrar de sempre passar uma lista como argumento dentro da função deste modulo
import deletar
import animacoes
import login

class Principal(Tk, Frame, Label, Entry, Button, Progressbar):
    def __init__(self):
        super().__init__()

        def login_usuarios():

            def logar():
                nome = entrada_nome.get()
                senha = entrada_senha.get()

                campos = verificador_campos_vazios.verificador([nome, senha])

                if campos:
                    status, msg = login.verificar_credenciais(nome, senha)
                    print(msg)

                    if status:
                        label_mensagem_status = Label(self.frame_resposta_interno, width=35, bg="green", text="login bem sucedido. Iniciando sessão.".upper(), font=("Arial Bold", 11), fg="white")
                        label_mensagem_status.place(x=230, y=20)

                    else:
                        label_mensagem_status = Label(self.frame_resposta_interno, width=35, bg="red", text=fr"{msg}".upper(), font=("Arial Bold", 11), fg="white")
                        label_mensagem_status.place(x=230, y=20)
 

                else:
                    label_mensagem_status = Label(self.frame_resposta_interno, width=35, bg="red", text="preencha os campos corretamente!".upper(), font=("Arial Bold", 11), fg="white")
                    label_mensagem_status.place(x=230, y=20)

            label_nome = Label(self.frame_resposta_interno, text="nome: ".upper())
            label_nome.place(x=15, y=20)
            
            entrada_nome = Entry(self.frame_resposta_interno)
            entrada_nome.place(x=70, y=20)
            
            label_senha = Label(self.frame_resposta_interno, text="senha: ".upper())
            label_senha.place(x=15, y=50)
            
            entrada_senha = Entry(self.frame_resposta_interno, show="*")
            entrada_senha.place(x=70, y=50)

            botao_login_usuario = Button(self.frame_resposta_interno, width=24, bg="lightblue", text="logar".upper(), command=logar)
            botao_login_usuario.place(x=16, y=80)

        def confirmar():
            
            self.valor = self.entrada_user.get()
            self.entrada_user.delete(0, END)
            print(type(self.valor))

            if self.valor == 0 or len(self.valor) == 0 or self.valor == " " or self.valor == "" or self.valor not in ["1","2","3","4"]:
                print("por favor, digite corretamente!")
                self.res = "[erro] por favor digite corretamente!".upper()
                self.label_resposta.configure(text=self.res)
                try:
                    for item in self.frame_resposta_interno.winfo_children():
                        item.destroy()

                except:
                    print("nenhum opção está selecionada no momento.")

            else:
                for item in self.frame_resposta_interno.winfo_children():
                    item.destroy()

                print("valor aceito: " + self.valor)
                self.res = fr"valor {self.valor} aceito. "
                
                if self.valor == "1":
                    self.label_resposta.configure(text="fazer login".upper())
                    log_login_usuario = login_usuarios()
                    

                elif self.valor == "2":
                    self.label_resposta.configure(text="cadastro de usuário".upper() )

                    # essa variável serva para caso exista um arquivo destinado a salvar logs de eventos no sistema (cadastro, exclusão de contas e logins) - contendo data,hora e tipo da operação
                    log_cadastrar_user = cadastrar_usuario()

                elif self.valor == "3":
                    self.label_resposta.configure(text="deletar conta de usuário".upper())
                    frameDeletar = FrameDeletar()

                else:
                    self.label_resposta.configure(text="visualizar contas".upper())

        def cadastrar_usuario():

            label_nome = Label(self.frame_resposta_interno, text="nome: ".upper())
            label_nome.place(x=15, y=20)
            
            entrada_nome = Entry(self.frame_resposta_interno)
            entrada_nome.place(x=70, y=20)
            
            label_senha = Label(self.frame_resposta_interno, text="senha: ".upper())
            label_senha.place(x=15, y=50)
            
            entrada_senha = Entry(self.frame_resposta_interno, show="*")
            entrada_senha.place(x=70, y=50)

            def get_entradas():
                nome = entrada_nome.get()
                senha = entrada_senha.get()

                verifica_campos = verificador_campos_vazios.verificador([nome, senha])
                if verifica_campos:

                    response = cadastrar.cadastrar(nome, senha) # se a resposta for positiva, aparecerá uma item na tela com uma resposta positiva para o usuário      

                    if response:
                        label_mensagem_status = Label(self.frame_resposta_interno, width=35, bg="green", text="usuário cadastrado com sucesso!".upper(), font=("Arial Bold", 11), fg="white")
                        label_mensagem_status.place(x=230, y=20)
                        entrada_nome.delete(0, END)
                        entrada_senha.delete(0, END)

                    else:
                        label_mensagem_status = Label(self.frame_resposta_interno, width=35, bg="red", text="usuário já está cadastrado!".upper(), font=("Arial Bold", 11), fg="white")
                        label_mensagem_status.place(x=230, y=20)
                        entrada_nome.delete(0, END)
                        entrada_senha.delete(0, END)
                
                else:
                    label_mensagem_status = Label(self.frame_resposta_interno, width=35, bg="red", text="preencha os campos corretamente!".upper(), font=("Arial Bold", 11), fg="white")
                    label_mensagem_status.place(x=230, y=20)

            botao_cadastrar_usuario = Button(self.frame_resposta_interno, width=24, bg="lightblue", text="cadastrar usuário".upper(), command=get_entradas)
            botao_cadastrar_usuario.place(x=16, y=80)

        # variável que armazena temporáriamente as credenciais do usuário

        self.configure(bg="#121212")
        self.geometry("700x600")
        self.title("janela principal")
        self.frame_principal = Frame(self, width=650, height=550, bg="#121212")
        self.frame_principal.pack(side=TOP)
        self.frame_principal.propagate(False)

        self.frame_principal_info_user = Frame(self.frame_principal, width=650, height=250, bg="#121212")
        self.frame_principal_info_user.pack(side=TOP)
        self.frame_principal_info_user.propagate(False)

        self.frame_principal_de_resposta = Frame(self.frame_principal, width=600, height=280, bg="#121212" )
        self.frame_principal_de_resposta.pack(side=BOTTOM)
        self.frame_principal_de_resposta.propagate(False)

        self.frame_painel_controle = Frame(self.frame_principal_info_user, width=300, height=40, bg="#121212")
        self.frame_painel_controle.place(x=0, y=0)
        self.frame_painel_controle.propagate(False)

        self.label_painel_controle = Label(self.frame_painel_controle, text="painel principal".upper(), font=("Arial bold", 20 ))
        self.label_painel_controle.pack(side=BOTTOM)
        self.label_painel_controle.propagate(False)

        self.frame_opcoes = Frame(self.frame_principal_info_user, width=300, height=200, bg="#121212")
        self.frame_opcoes.pack(side=BOTTOM)
        self.frame_opcoes.propagate(False)

        self.label_opcoes_titulo = Label(self.frame_opcoes, width=300, height=20, background="lightgray", text="gerenciador".upper(), font=("Arial bold", 13))
        self.label_opcoes_titulo.place(x = 10, y = 10, width=280, height=20)
        self.label_opcoes_titulo.propagate(False)

        self.frame_opcoes_corpo = Frame(self.frame_opcoes, width=300, height=160, bg="#121212")
        self.frame_opcoes_corpo.pack(side=BOTTOM)
        self.frame_opcoes_corpo.propagate(False)

        self.frame_opcoes_corpo_interno = Frame(self.frame_opcoes_corpo, width=250, height=110, bg="lightgray")
        self.frame_opcoes_corpo_interno.pack(pady=5)
        self.frame_opcoes_corpo_interno.propagate(False)

        self.label_opcao_1 = Label(self.frame_opcoes_corpo_interno, width=30, text="1 - Fazer login")
        self.label_opcao_1.pack(side=TOP, pady=5)

        self.label_opcao_2 = Label(self.frame_opcoes_corpo_interno, width=30, text="2 - Criar usuário")
        self.label_opcao_2.pack(side=TOP)

        self.label_opcao_3 = Label(self.frame_opcoes_corpo_interno, width=30, text="3 - Deletar usuário")
        self.label_opcao_3.pack(side=TOP, pady=5)

        self.label_opcao_4 = Label(self.frame_opcoes_corpo_interno, width=30, text="4 - Visualizar contas")
        self.label_opcao_4.pack(side=TOP)

        # serve para configurar o frame_opcoes_corpo para centralizar todo o texto
        self.frame_opcoes_corpo.columnconfigure(index=0, weight=1)
        self.frame_opcoes_corpo.columnconfigure(index=1, weight=0)

        self.frame_opcoes_entrada_user = Frame(self.frame_opcoes_corpo, width=250, height=40, bg="lightgray")
        self.frame_opcoes_entrada_user.pack(side=BOTTOM)
        self.frame_opcoes_entrada_user.propagate(False)

        self.entrada_user = Entry(self.frame_opcoes_entrada_user, width=25)
        self.entrada_user.place(x=10, y=11)

        self.botao_confirma_entrada_user = Button(self.frame_opcoes_entrada_user, bg="lightblue", text="confirmar", command=confirmar)
        self.botao_confirma_entrada_user.place(x=175, y=8)
        self.botao_confirma_entrada_user.propagate(False)

        self.label_resposta = Label(self.frame_principal_de_resposta, width=83, fg="red")
        self.label_resposta.place(x=5, y=10)

        self.frame_resposta_interno = Frame(self.frame_principal_de_resposta, width=585, height=230, bg="lightgray")
        self.frame_resposta_interno.place(x=6, y=40)
        self.frame_resposta_interno.propagate(False)
        self.frame_resposta_interno.grid_propagate(False)

# essa classe serve para estilizar o frame deletar e os seus respectivos widgets (para não misturar com a Principal() )

class FrameDeletar():
    def __init__(self):

        def pegar_valor_selecionado():
            
            limpar_frame = self.frame_retorno_interno_resposta.winfo_children()
            print(limpar_frame)

            indice_selecionado = self.listbox_usuarios.curselection()

            if indice_selecionado:
                
                valor_selecionado = self.listbox_usuarios.get(indice_selecionado)
                print(valor_selecionado)

                status_deletar = deletar.deletar_usuario(valor_selecionado)

                if status_deletar:
                    # gambiarra necessária
                    self.label_resposta.configure(text="")
                    self.label_status.configure(text="", bg="lightblue")
                    self.frame_retorno_interno_resposta.update()
                    # --------------------

                    self.label_resposta.configure(text=f"deletando o usuário [{valor_selecionado[5:]}]")
                    self.label_resposta.pack()
                    self.label_status.configure(text="executando operação...", fg="red", bg="lightblue")
                    self.label_status.pack(pady=10)
                    self.barra_progresso.pack()

                    animacoes.carregamento(self.barra_progresso, janela)

                    self.label_resposta.configure(text=f"usuário [{valor_selecionado[5:]}] deletado!")
                    self.label_status.configure(text="operação bem sucedida!", fg="green")

                    # abaixo, serve para atualizar os valores de listbox
                    
                    self.listbox_usuarios.delete(0, END)

                    self.todos_usuarios = deletar.visualizar()

                    self.listbox_usuarios.insert(0, "ID    USUÁRIO")

                    for item in self.todos_usuarios:
                        self.listbox_usuarios.insert(END, item.upper())

                    self.listbox_usuarios.itemconfig(0, {"bg":"lightgray"})

            else:
                print("nenhum indice foi selecionado!")
                self.label_resposta.configure(text="[Erro]")
                self.label_resposta.pack()
                self.label_status.configure(text="nenhum item foi selecionado!", fg="red")
                self.label_status.pack()

        self.frame_retorno_interno = Frame(janela.frame_resposta_interno, width=575, height=220, bg="lightblue")
        self.frame_retorno_interno.place(x=5, y=5)
        self.frame_retorno_interno.propagate(False)

        self.frame_retorno_interno_resposta = Frame(self.frame_retorno_interno, width=250, height=200, bg="lightblue")
        self.frame_retorno_interno_resposta.place(x= 310, y=10)
        self.frame_retorno_interno_resposta.propagate(False)
        self.frame_retorno_interno_resposta.pack_propagate(False)

        # ABAIXO, é tudo o que vai aparecer e deseparecer com base na interação com o usuário (que tenha relação com 'deletar o usuário')
        self.label_resposta = Label(self.frame_retorno_interno_resposta, width=200)
        self.label_resposta.pack_forget()

        self.label_status = Label(self.frame_retorno_interno_resposta, fg="red" , width=200, bg="lightgray" ,font=("Arial bold", 11))
        self.label_status.pack_forget()

        self.barra_progresso = Progressbar(self.frame_retorno_interno_resposta, length=200, orient="horizontal")
        self.barra_progresso.pack_forget()

        self.listbox_usuarios = Listbox(janela.frame_resposta_interno, width=40, selectmode="single", borderwidth=0)
        self.todos_usuarios = deletar.visualizar()
        self.todos_usuarios.insert(0, "ID    USUÁRIO")

        for item in self.todos_usuarios:
            self.listbox_usuarios.insert(END, item.upper())

        self.listbox_usuarios.itemconfig(0, {"bg":"lightgray"})
        
        self.listbox_usuarios.place(x=40, y=15)
        self.botao_deletar = Button(self.frame_retorno_interno, width=30, bg="lightgray", text="deletar usuário".upper(), command=pegar_valor_selecionado)
        self.botao_deletar.place(x=45, y=180)

janela = Principal()
janela.mainloop()