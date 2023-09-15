from customtkinter import *

from visao.pessoa_visao import PessoaVisao
from visao.usuario_visao import UsuarioVisao

from controle.pessoa_cont import PessoaControle
from controle.usuario_cont import UsuarioControle

class MainVisao:
    def __init__(self):
        self.pessoa_controle = PessoaControle()
        self.usuario_controle = UsuarioControle()

    def menu(self):
        def menu_logado(tipo_user):
            limpa_tela()
            tela_logado = CTkFrame(root)
            tela_logado.grid()
            btn_pessoa = CTkButton(tela_logado, text="PESSOA", command= lambda: pessoa_visao.menu(tipo_user))
            btn_pessoa.grid(pady=10, padx=10)
            if tipo_user == 2:
                btn_user = CTkButton(tela_logado, text="USUÁRIO", command= lambda: usuario_visao.menu(tipo_user))
                btn_user.grid(pady=10, padx=10)
            btn_voltar = CTkButton(tela_logado, text="VOLTAR", command=menu_inicial)
            btn_voltar.grid(pady=10, padx=10)

        def limpa_tela():
            for widget in root.winfo_children():
                widget.grid_remove()
        
        def menu_inicial():
            limpa_tela()

            container = CTkFrame(root)
            container.grid()

            btn_user  = CTkButton(container, text="TELA DE LOGIN", command=expand_options)
            btn_user.grid(pady=10, padx=10)
            btn_sair = CTkButton(container, text="SAIR DO PROGRAMA", command=root.destroy)
            btn_sair.grid(pady=10, padx=10)

        def expand_options():
            def cadastro_user():
                usuario_visao.gravar(pessoa_visao)

            def checa_bd():
                user_get = texto_user.get()
                senha_get = texto_senha.get()
                achou = self.usuario_controle.buscar(user_get, senha_get)
                print(f"Achou: {achou}")
                if achou:
                    menu_logado(achou)
                else:
                    nao_achou = CTkToplevel()
                    nao_achou.title("NÃO ACHOU")
                    nao_achou_label = CTkLabel(nao_achou, text="Usuário não encontrado").grid(pady=10, padx=10)
                    ok_button = CTkButton(nao_achou, text="OK", command=nao_achou.destroy)
                    ok_button.grid(pady=10, padx=10)
            limpa_tela()
            container = CTkFrame(root)
            container.grid(row=0, column=0)

            label_user = CTkLabel(container, text="USUARIO:")
            texto_user = CTkEntry(container)
            label_senha = CTkLabel(container, text="SENHA:")
            texto_senha = CTkEntry(container, show="*")
            btn_login = CTkButton(container, text="LOGIN", command=checa_bd)
            btn_cadastrar = CTkButton(container, text="CADASTRAR", command=cadastro_user)
            btn_voltar = CTkButton(container, text="VOLTAR", command= menu_inicial)

            label_user.grid(row=0, column=0, sticky=W, padx=10, pady=10)
            texto_user.grid(row=0, column=1, padx=10, pady=10)
            label_senha.grid(row=1, column=0, sticky=W, padx=10, pady=10)
            texto_senha.grid(row=1, column=1, padx=10, pady=10)
            btn_login.grid(row=2, column=0, columnspan=2, pady=10)
            btn_voltar.grid(row=3, column=0, columnspan=2, pady=10)
            btn_cadastrar.grid(row=4, column=0, columnspan=2, pady=10)
        
        root = CTk()
        root.geometry("350x450")
        root.title('MENU INICIAL - GERENCIAMENTO DE TIME')
        root.resizable(0, 0)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        menu_inicial()
        pessoa_visao = PessoaVisao(self.pessoa_controle)
        usuario_visao = UsuarioVisao(self.usuario_controle)
        
        root.mainloop()
