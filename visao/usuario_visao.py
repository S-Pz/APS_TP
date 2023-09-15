from tkinter.ttk import Treeview
from customtkinter import *

from visao.visao import Visao
from controle.controle import Controle
from controle.usuario_cont import UsuarioControle
from controle.pessoa_cont import PessoaControle
from modelo.usuario import Usuario

class UsuarioVisao(Visao):
    def __init__(self, controle: Controle):
        super().__init__(controle)

    def limpa_tela(self):
        for widget in top_user.winfo_children():
            widget.grid_remove()

    def menu_inicial_user(self):
        pass

    def menu(self, tipo_user: int):
        global top_user
        top_user = CTk()
        top_user.geometry("350x450")
        top_user.title("MENU DE USUÁRIOS")
        container = CTkFrame(top_user)
        container.grid()
        top_user.resizable(0, 0)
        top_user.columnconfigure(0, weight=1)
        top_user.rowconfigure(0, weight=1)

        user_voltar = CTkButton(container, text="VOLTAR AO MENU INICIAL", command=top_user.destroy).grid(pady=10, padx=10)
        if tipo_user == 2:
            user_ins = CTkButton(container, text="INSERIR USUÁRIO", command=self.gravar).grid(pady=10, padx=10)
            user_exc = CTkButton(container, text="EXCLUIR USUÁRIO", command=self.apagar).grid(pady=10, padx=10)
        user_bID = CTkButton(container, text="BUSCAR USUÁRIO", command=self.buscar).grid(pady=10, padx=10)
        btn_voltar = CTkButton(top_user, text="VOLTAR", command=top_user.destroy).grid(pady=10, padx=10)

    def gravar(self, pessoa_visao):
        def cadastro_pessoa():
            pessoa_visao.gravar()

        def persistir():
            tipo = "NORMAL"
            login = texto_id.get()
            senha = texto_senha.get()
            confirma = texto_confirma.get()
            if senha != confirma:
                nao_confere = CTkToplevel()
                nao_confere.title("SENHAS ERRADAS")
                lbl_nao_confere = CTkLabel(nao_confere, text="AS SENHAS NÃO CONFEREM").grid(pady=10, padx=10)
                btn_nao_confere = CTkButton(nao_confere, text="OK", command=nao_confere.destroy).grid(pady=10, padx=10)

                print("As senhas não conferem")
            else:
                usuario = Usuario(login, senha, tipo)
                salvou_ou_nao = self.controle.gravar(usuario)
                gravou_janela = CTkToplevel()
                if salvou_ou_nao:
                    gravou_janela.title("CADASTRO BEM SUCEDIDO")
                    label_gravou = CTkLabel(gravou_janela, text="USUÁRIO CADASTRADO COM SUCESSO").grid(pady=10, padx=10)
                    cadastro_pessoa()
                else:
                    gravou_janela.title("CADASTRO NÃO REALIZADO")
                    label_nao_gravou = CTkLabel(gravou_janela, text="REVISE OS DADOS").grid(pady=10, padx=10)
                btn_gravou = CTkButton(gravou_janela, text="OK", command=gravou_janela.destroy).grid(pady=10, padx=10)

        top_user_gravar = CTk()
        top_user_gravar.title("INSERIR USUÁRIO")

        container = CTkFrame(top_user_gravar)
        container.grid()

        lbl_id_user = CTkLabel(container, text="DIGITE O CPF DO USUÁRIO").grid(pady=10, padx=10)
        texto_id = CTkEntry(container, font=("Helvetica", 18))
        texto_id.grid(pady=10, padx=10)

        lbl_user_senha = CTkLabel(container, text="DIGITE A SENHA DO USUÁRIO").grid(pady=10, padx=10)
        texto_senha = CTkEntry(container, font=("Helvetica", 18))
        texto_senha.grid(pady=10, padx=10)

        lbl_senha_confirma = CTkLabel(container, text="CONFIRME A SENHA DO USUÁRIO").grid(pady=10, padx=10)
        texto_confirma = CTkEntry(container, font=("Helvetica", 18))
        texto_confirma.grid(pady=10, padx=10)

        btn_cadastrar = CTkButton(container, text="CADASTRAR USUÁRIO", command=persistir).grid(pady=10, padx=10)
        btn_voltar = CTkButton(container, text="VOLTAR", command=container.destroy).grid(pady=10, padx=10)

    def apagar(self):  # virar CTkEntry
        def exclui():
            user_id = texto_id.get()
            if self.controle.apagar(user_id):
                ok_exc = CTkToplevel()
                ok_exc.title("")
                lbl_ok = CTkLabel(ok_exc, text="USUÁRIO EXCLUÍDO COM SUCESSO").grid()
                btn_ok = CTkButton(ok_exc, text="OK", command=ok_exc.destroy).grid()
                top_user_exclusao.destroy()
            else:
                ok_exc = CTkToplevel()
                ok_exc.title("")
                lbl_ok = CTkLabel(ok_exc, text="Não há um usuário com esse ID.").grid()
                btn_ok = CTkButton(ok_exc, text="OK", command=ok_exc.destroy).grid()

        top_user_exclusao = CTkToplevel()
        top_user_exclusao.title("EXCLUIR USUÁRIO")

        lbl_id_user = CTkLabel(top_user_exclusao, text="DIGITE O CPF DO USUÁRIO").grid()
        texto_id = CTkEntry(top_user_exclusao, font=("Helvetica", 18))
        texto_id.grid(pady=10)

        btn_insere = CTkButton(top_user_exclusao, text="EXCLUIR USUÁRIO", command=exclui).grid()
        btn_voltar = CTkButton(top_user_exclusao, text="VOLTAR",command=top_user_exclusao.destroy).grid()

    def buscar(self):
        def procura():
            termo = texto_id.get()
            achados = self.controle.buscar(termo)
            janela_achados = CTkToplevel()
            janela_achados.title("RESULTADO DA PESQUISA")
            janela_achados.geometry("600x600")

            frame_pesquisa = CTkFrame(janela_achados)
            frame_pesquisa.pack(pady=10, padx=10)

            scroll = CTkScrollbar(frame_pesquisa)
            scroll.pack(side=RIGHT, fill=Y)

            scroll = CTkScrollbar(frame_pesquisa, orientation='horizontal')
            scroll.pack(side=BOTTOM, fill=X)

            resultado = Treeview(frame_pesquisa, yscrollcommand=scroll.set, xscrollcommand=scroll.set)
            resultado.pack(pady=10, padx=10)

            scroll.configure(command=resultado.yview)
            scroll.configure(command=resultado.xview)

            resultado['columns'] = ('tipo', 'login')
            resultado.column("#0", width=0,  stretch=NO)
            resultado.column("tipo",anchor=CENTER, width=80)
            resultado.column("login",anchor=CENTER,width=80)

            resultado.heading("#0",text="",anchor=CENTER)
            resultado.heading("tipo",text="Tipo de usuário",anchor=CENTER)
            resultado.heading("login",text="Login",anchor=CENTER)

            for (indice, pessoa) in enumerate(achados):
                resultado.insert(parent='',index='end',iid=indice,text='',
                                 values=(pessoa[0],pessoa[1]))

            lbl_janela = CTkLabel(janela_achados, text="RESULTADO DA PESQUISA").pack(pady=10, padx=10)

            btn_ok = CTkButton(janela_achados, text="OK", command=janela_achados.destroy).pack(pady=10, padx=10)

        self.limpa_tela()
        top_user_buscar = CTkFrame(top_user)
        top_user_buscar.grid(pady=10, padx=10)

        lbl_id_user = CTkLabel(top_user_buscar, text="DIGITE O NOME DO PESSOA").grid(pady=10, padx=10)
        texto_id = CTkEntry(top_user_buscar, font=("Helvetica", 18))
        texto_id.grid(pady=10)

        btn_buscar = CTkButton(top_user_buscar, text="BUSCAR", command=procura)
        btn_buscar.grid(pady=10, padx=10)
        btn_voltar = CTkButton(top_user_buscar, text="VOLTAR", command=self.menu_inicial_user)
        btn_voltar.grid(pady=10, padx=10)
