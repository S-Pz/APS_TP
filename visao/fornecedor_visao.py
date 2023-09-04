from tkinter import *
from visao.visao import Visao
from controle.controle import Controle
from modelo.fornecedor import Fornecedor


class FornecedorVisao(Visao):
    def __init__(self, controle: Controle):
        super().__init__(controle)

    def menu(self):
        top_cli = Toplevel()
        top_cli.geometry("250x200")
        top_cli.title("MENU DE CLIENTES")
        cli_voltar = Button(top_cli, text="VOLTAR AO MENU INICIAL", command=top_cli.destroy).pack(ipadx=150)
        cli_ins = Button(top_cli, text="INSERIR CLIENTE", command=self.insercao).pack(ipadx=150)
        cli_exc = Button(top_cli, text="EXCLUIR CLIENTE", command=self.exclusao).pack(ipadx=150)
        cli_alt = Button(top_cli, text="ALTERAR CLIENTE", command=self.alteracao).pack(ipadx=150)
        cli_bID = Button(top_cli, text="BUSCAR CLIENTE POR ID", command=self.buscaID).pack(ipadx=150)
        cli_bVAL = Button(top_cli, text="BUSCAR CLIENTE POR NOME", command=self.buscaVal).pack(ipadx=150)

    def gravar(self):  # virar Entry
        def insere():
            cli_id = int(texto_id.get())
            cli_nome = texto_nome.get()
            cli_cpf = texto_cpf.get()
            entidade = Jogador(cli_id, cli_nome, cli_cpf)
            self.controle.insercao(entidade)
            ok_exc = Toplevel()
            ok_exc.title("")
            lbl_ok = Label(ok_exc, text="CLIENTE INSERIDO COM SUCESSO").pack()
            btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
            top_cli_insercao.destroy()

        top_cli_insercao = Toplevel()
        top_cli_insercao.title("INSERIR CLIENTE")

        lbl_id_cli = Label(top_cli_insercao, text="DIGITE O ID DO CLIENTE").pack()
        texto_id = Entry(top_cli_insercao, font=("Helvetica", 18))
        texto_id.pack(pady=10)

        lbl_cli_nome = Label(top_cli_insercao, text="DIGITE O NOME DO CLIENTE").pack()
        texto_nome = Entry(top_cli_insercao, font=("Helvetica", 18))
        texto_nome.pack(pady=10)

        lbl_cli_cpf = Label(top_cli_insercao, text="DIGITE O CPF DO CLIENTE").pack()
        texto_cpf = Entry(top_cli_insercao, font=("Helvetica", 18))
        texto_cpf.pack(pady=10)

        btn_insere = Button(top_cli_insercao, text="INSERIR CLIENTE", command=insere).pack()
        btn_voltar = Button(top_cli_insercao, text="VOLTAR", command=top_cli_insercao.destroy).pack()

    def apagar(self):  # virar Entry
        def exclui():
            cli_id = int(texto_id.get())
            if self.controle.buscaID(cli_id) != -1:
                self.controle.exclusao(self.controle.buscaID(cli_id))
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text="CLIENTE EXCLUÍDO COM SUCESSO").pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
                top_cli_exclusao.destroy()
            else:
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text="Não há um cliente com esse ID.").pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
        top_cli_exclusao = Toplevel()
        top_cli_exclusao.title("EXCLUIR CLIENTE")

        lbl_id_cli = Label(top_cli_exclusao, text="DIGITE O ID DO CLIENTE").pack()
        texto_id = Entry(top_cli_exclusao, font=("Helvetica", 18))
        texto_id.pack(pady=10)

        btn_insere = Button(top_cli_exclusao, text="EXCLUIR CLIENTE", command=exclui).pack()
        btn_voltar = Button(top_cli_exclusao, text="VOLTAR",command=top_cli_exclusao.destroy).pack()

    def buscar(self):
        def bid():
            cli_id = int(texto_id.get())
            if self.controle.buscaID(cli_id) != -1:
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text=self.controle.buscaID(cli_id).__str__()).pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
            else:
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text="Não há um cliente com esse ID.").pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
        top_cli_bID = Toplevel()
        top_cli_bID.title("BUSCA POR ID")

        lbl_id_cli = Label(top_cli_bID, text="DIGITE O ID DO CLIENTE").pack()
        texto_id = Entry(top_cli_bID, font=("Helvetica", 18))
        texto_id.pack(pady=10)

        btn_insere = Button(top_cli_bID, text="BUSCAR", command=bid).pack()
        btn_voltar = Button(top_cli_bID, text="VOLTAR",command=top_cli_bID.destroy).pack()
