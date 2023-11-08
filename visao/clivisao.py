from tkinter import *
from visao.visao import Visao
from controle.controle import Controle
from modelo.cliente import Cliente


class ClienteVisao(Visao):
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

    def insercao(self):  # virar Entry
        def insere():
            cli_id = int(texto_id.get())
            cli_nome = texto_nome.get()
            cli_cpf = texto_cpf.get()
            entidade = Cliente(cli_id, cli_nome, cli_cpf)
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

    def exclusao(self):  # virar Entry
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

    def alteracao(self):
        def alterar():
            cli_id = int(texto_id.get())
            achou_cli = self.controle.buscaID(cli_id)
            if achou_cli != -1:
                escolha = alt.get()
                if escolha == 1:
                    def alt_in():
                        alterado = novo_nome.get()
                        entidade = Cliente(cli_id, alterado, achou_cli.cpf)
                        self.controle.alteracao(entidade)
                        ok_exc = Toplevel()
                        ok_exc.title("")
                        lbl_ok = Label(ok_exc, text="Nome do cliente alterado com sucesso.").pack()
                        btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
                        top_alt_nome.destroy()
                        top_cli_alteracao.destroy()

                    top_alt_nome = Toplevel()
                    lbl_novo_nome = Label(top_alt_nome, text="DIGITE O NOVO NOME").pack()
                    novo_nome = Entry(top_alt_nome, font=("Helvetica", 18))
                    novo_nome.pack(pady=10)
                    btn_voltar = Button(top_alt_nome, text="ALTERAR NOME",
                                        command=alt_in).pack()

                if escolha == 2:
                    def alt_in():
                        alterado = novo_cpf.get()
                        entidade = Cliente(cli_id, achou_cli.nome, alterado)
                        self.controle.alteracao(entidade)
                        ok_exc = Toplevel()
                        ok_exc.title("")
                        lbl_ok = Label(ok_exc, text="CPF do cliente alterado com sucesso.").pack()
                        btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
                        top_alt_cpf.destroy()
                        top_cli_alteracao.destroy()

                    top_alt_cpf = Toplevel()
                    lbl_novo_cpf = Label(top_alt_cpf, text="DIGITE O NOVO CPF").pack()
                    novo_cpf = Entry(top_alt_cpf, font=("Helvetica", 18))
                    novo_cpf.pack(pady=10)
                    btn_voltar = Button(top_alt_cpf, text="ALTERAR CPF",
                                        command=alt_in).pack()
            else:
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text="Não há um cliente com esse ID.").pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()

        top_cli_alteracao = Toplevel()
        top_cli_alteracao.title("ALTERAR CLIENTE")

        lbl_id_cli = Label(top_cli_alteracao, text="DIGITE O ID DO CLIENTE").pack()
        texto_id = Entry(top_cli_alteracao, font=("Helvetica", 18))
        texto_id.pack(pady=10)

        alt = IntVar()
        Radiobutton(top_cli_alteracao, text="ALTERAR NOME", variable=alt, value=1).pack()
        Radiobutton(top_cli_alteracao, text="ALTERAR CPF", variable=alt, value=2).pack()

        btn_insere = Button(top_cli_alteracao, text="ALTERAR CLIENTE", command=alterar).pack()
        btn_voltar = Button(top_cli_alteracao, text="VOLTAR",command=top_cli_alteracao.destroy).pack()

    def buscaID(self):
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

    def buscaVal(self):
        def bval():
            cli_Val = texto_val.get()
            if self.controle.buscaVal(cli_Val) != -1:
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text=self.controle.buscaVal(cli_Val).__str__()).pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
            else:
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text="Não há um cliente com esse nome.").pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()

        top_cli_bVal = Toplevel()
        top_cli_bVal.title("BUSCA POR NOME")

        lbl_id_cli = Label(top_cli_bVal, text="DIGITE O NOME DO CLIENTE").pack()
        texto_val = Entry(top_cli_bVal, font=("Helvetica", 18))
        texto_val.pack(pady=10)

        btn_insere = Button(top_cli_bVal, text="BUSCAR", command=bval).pack()
        btn_voltar = Button(top_cli_bVal, text="VOLTAR", command=top_cli_bVal.destroy).pack()
