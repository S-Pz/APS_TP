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

    def chama_menu(self, tipo_user):
        global top_usuario
        top_usuario = CTk()
        top_usuario.geometry("350x450")
        top_usuario.resizable(0, 0)
        top_usuario.columnconfigure(0, weight=1)
        top_usuario.rowconfigure(0, weight=1)
        top_usuario.title("MENU DE USUÁRIO")
        self.menu(tipo_user)

    def limpa_tela(self):
        for widget in top_usuario.winfo_children():
            widget.grid_remove()

    def menu(self, tipo_user: int):
        self.limpa_tela()
        container = CTkFrame(top_usuario)
        container.grid()
        top_usuario.resizable(0, 0)
        top_usuario.columnconfigure(0, weight=1)
        top_usuario.rowconfigure(0, weight=1)

        user_buscar  = CTkButton(container, text="BUSCAR USUÁRIO", command=self.buscar).grid(pady=10, padx=10)
        user_voltar = CTkButton(container, text="VOLTAR AO MENU INICIAL", command=top_usuario.destroy).grid(pady=10, padx=10)

    def gravar(self, nome_pessoa):
        def persistir():
            nome = nome_pessoa
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
                usuario = Usuario(nome, login, senha, tipo)
                salvou_ou_nao = self.controle.gravar(usuario)
                gravou_janela = CTkToplevel()
                if salvou_ou_nao:
                    gravou_janela.title("CADASTRO BEM SUCEDIDO")
                    label_gravou = CTkLabel(gravou_janela, text="USUÁRIO CADASTRADO COM SUCESSO").grid(pady=10, padx=10)
                    btn_gravou = CTkButton(gravou_janela, text="OK", command= lambda: [gravou_janela.destroy(), top_usuario_gravar.destroy()]).grid(pady=10, padx=10)
                else:
                    gravou_janela.title("CADASTRO NÃO REALIZADO")
                    label_nao_gravou = CTkLabel(gravou_janela, text="REVISE OS DADOS").grid(pady=10, padx=10)
                    btn_gravou = CTkButton(gravou_janela, text="OK", command=gravou_janela.destroy).grid(pady=10, padx=10)

        top_usuario_gravar = CTk()
        top_usuario_gravar.title("INSERIR USUÁRIO")

        container = CTkFrame(top_usuario_gravar)
        container.grid()

        lbl_id_user = CTkLabel(container, text="DIGITE O USERNAME").grid(pady=10, padx=10)
        texto_id = CTkEntry(container, font=("Helvetica", 18))
        texto_id.grid(pady=10, padx=10)

        lbl_user_senha = CTkLabel(container, text="DIGITE A SENHA DO USUÁRIO").grid(pady=10, padx=10)
        texto_senha = CTkEntry(container, font=("Helvetica", 18), show="*")
        texto_senha.grid(pady=10, padx=10)

        lbl_senha_confirma = CTkLabel(container, text="CONFIRME A SENHA DO USUÁRIO").grid(pady=10, padx=10)
        texto_confirma = CTkEntry(container, font=("Helvetica", 18), show="*")
        texto_confirma.grid(pady=10, padx=10)

        btn_cadastrar = CTkButton(container, text="CADASTRAR USUÁRIO", command=persistir).grid(pady=10, padx=10)
        #btn_voltar = CTkButton(container, text="VOLTAR", command=container.destroy).grid(pady=10, padx=10)

    def apagar(self): 
        def exclui():
            user_id = texto_id.get()
            if self.controle.apagar(user_id):
                ok_exc = CTkToplevel()
                ok_exc.title("")
                lbl_ok = CTkLabel(ok_exc, text="USUÁRIO EXCLUÍDO COM SUCESSO").grid()
                btn_ok = CTkButton(ok_exc, text="OK", command=ok_exc.destroy).grid()
                top_usuario_exclusao.destroy()
            else:
                ok_exc = CTkToplevel()
                ok_exc.title("")
                lbl_ok = CTkLabel(ok_exc, text="Não há um usuário com esse ID.").grid()
                btn_ok = CTkButton(ok_exc, text="OK", command=ok_exc.destroy).grid()

        top_usuario_exclusao = CTkToplevel()
        top_usuario_exclusao.title("EXCLUIR USUÁRIO")

        lbl_id_user = CTkLabel(top_usuario_exclusao, text="DIGITE O USERNAME DO USUÁRIO").grid()
        texto_id = CTkEntry(top_usuario_exclusao, font=("Helvetica", 18))
        texto_id.grid(pady=10)

        btn_insere = CTkButton(top_usuario_exclusao, text="EXCLUIR USUÁRIO", command=exclui).grid()
        btn_voltar = CTkButton(top_usuario_exclusao, text="VOLTAR",command=top_usuario_exclusao.destroy).grid()

    def buscar(self):
        def procura():
            termo = texto_id.get()
            achados = self.controle.buscar(termo)
            if achados:
                janela_achados = CTkToplevel()
                janela_achados.title("RESULTADO DA PESQUISA")
                janela_achados.geometry("1000x600")

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

                resultado['columns'] = ('tipo', 'login', 'senha')
                resultado.column("#0", width=0,  stretch=NO)
                resultado.column("tipo",anchor=CENTER, width=80)
                resultado.column("login",anchor=CENTER,width=80)
                resultado.column("senha",anchor=CENTER,width=80)

                resultado.heading("#0",text="",anchor=CENTER)
                resultado.heading("tipo",text="Username",anchor=CENTER)
                resultado.heading("login",text="Tipo",anchor=CENTER)
                resultado.heading("senha",text="Senha",anchor=CENTER)

                for (indice, pessoa) in enumerate(achados):
                    resultado.insert(parent='',index='end',iid=indice,text='',
                                     values=(pessoa[0],pessoa[1],pessoa[2]))

                lbl_janela = CTkLabel(janela_achados, text="RESULTADO DA PESQUISA").pack(pady=10, padx=10)

                btn_ok = CTkButton(janela_achados, text="OK", command=janela_achados.destroy).pack(pady=10, padx=10)
            else:
                nao_achou = CTkToplevel()
                nao_achou_lbl = CTkLabel(nao_achou, text="Não achou o usuário")
                nao_achou_btn = CTkButton(nao_achou, text="OK", command=nao_achou.destroy)

        self.limpa_tela()
        top_usuario_buscar = CTkFrame(top_usuario)
        top_usuario_buscar.grid(pady=10, padx=10)

        lbl_id_user = CTkLabel(top_usuario_buscar, text="DIGITE O USERNAME DO USUÁRIO").grid(pady=10, padx=10)
        texto_id = CTkEntry(top_usuario_buscar, font=("Helvetica", 18))
        texto_id.grid(pady=10)

        btn_buscar = CTkButton(top_usuario_buscar, text="BUSCAR", command=procura)
        btn_buscar.grid(pady=10, padx=10)
        btn_voltar = CTkButton(top_usuario_buscar, text="VOLTAR", command=lambda: self.menu(2))
        btn_voltar.grid(pady=10, padx=10)
