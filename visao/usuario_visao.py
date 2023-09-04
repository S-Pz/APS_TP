from customtkinter import *

from visao.visao import Visao
from controle.controle import Controle
from controle.usuario_cont import UsuarioControle
from modelo.usuario import Usuario

class UsuarioVisao(Visao):
    def __init__(self, controle: Controle):
        super().__init__(controle)

    def menu(self, tipo_user: int):
        def expand_options():
            for widget in root.winfo_children():
                widget.grid_remove()

        top_user = CTkToplevel()
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
        #btn_voltar = CTkButton(top_user, text="VOLTAR", command=).grid(pady=10, padx=10)

    def gravar(self):
        for widget in root.winfo_children():
            widget.grid_remove()
        top_user_insercao = CTkToplevel()
        top_user_insercao.title("INSERIR USUÁRIO")

        lbl_id_user = CTkLabel(top_user_insercao, text="DIGITE O CPF DO USUÁRIO").grid()
        texto_id = CTkEntry(top_user_insercao, font=("Helvetica", 18))
        texto_id.grid(pady=10)

        lbl_user_nome = CTkLabel(top_user_insercao, text="DIGITE O NOME DO USUÁRIO").grid()
        texto_nome = CTkEntry(top_user_insercao, font=("Helvetica", 18))
        texto_nome.grid(pady=10)

        lbl_user_valor = CTkLabel(top_user_insercao, text="DIGITE O VALOR DO USUÁRIO").grid()
        texto_valor = CTkEntry(top_user_insercao, font=("Helvetica", 18))
        texto_valor.grid(pady=10)

        btn_insere = CTkButton(top_user_insercao, text="INSERIR USUÁRIO", command=insere).grid()
        btn_voltar = CTkButton(top_user_insercao, text="VOLTAR", command=top_user_insercao.destroy).grid()

    def apagar(self):  # virar CTkEntry
        def exclui():
            user_id = int(texto_id.get())
            if self.controle.buscar(user_id) != -1:
                self.controle.exclusao(self.controle.buscar(user_id))
                ok_exc = CTkToplevel()
                ok_exc.title("")
                lbl_ok = CTkLabel(ok_exc, text="USUÁRIO EXCLUÍDO COM SUCESSO").grid()
                btn_ok = CTkButton(ok_exc, text="OK", command=ok_exc.destroy).grid()
                top_user_exclusao.destroy()
            else:
                ok_exc = CTkToplevel()
                ok_exc.title("")
                lbl_ok = CTkLabel(ok_exc, text="Não há um useruto com esse ID.").grid()
                btn_ok = CTkButton(ok_exc, text="OK", command=ok_exc.destroy).grid()
        top_user_exclusao = CTkToplevel()
        top_user_exclusao.title("EXCLUIR USUÁRIO")

        lbl_id_user = CTkLabel(top_user_exclusao, text="DIGITE O ID DO USUÁRIO").grid()
        texto_id = CTkEntry(top_user_exclusao, font=("Helvetica", 18))
        texto_id.grid(pady=10)

        btn_insere = CTkButton(top_user_exclusao, text="EXCLUIR USUÁRIO", command=exclui).grid()
        btn_voltar = CTkButton(top_user_exclusao, text="VOLTAR",command=top_user_exclusao.destroy).grid()

    def buscar(self):
        def bid():
            user_id = int(texto_id.get())
            if self.controle.buscar(user_id) != -1:
                ok_exc = CTkToplevel()
                ok_exc.title("")
                lbl_ok = CTkLabel(ok_exc, text=self.controle.buscar(user_id).__str__()).grid()
                btn_ok = CTkButton(ok_exc, text="OK", command=ok_exc.destroy).grid()
            else:
                ok_exc = CTkToplevel()
                ok_exc.title("")
                lbl_ok = CTkLabel(ok_exc, text="Não há um useruto com esse ID.").grid()
                btn_ok = CTkButton(ok_exc, text="OK", command=ok_exc.destroy).grid()
        top_user_bID = CTkToplevel()
        top_user_bID.title("BUSCA POR ID")

        lbl_id_user = CTkLabel(top_user_bID, text="DIGITE O ID DO USUÁRIO").grid()
        texto_id = CTkEntry(top_user_bID, font=("Helvetica", 18))
        texto_id.grid(pady=10)

        btn_insere = CTkButton(top_user_bID, text="BUSCAR", command=bid).grid()
        btn_voltar = CTkButton(top_user_bID, text="VOLTAR",command=top_user_bID.destroy).grid()
