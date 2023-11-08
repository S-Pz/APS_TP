from tkinter import *
from visao.visao import Visao
from controle.controle import Controle
from modelo.venda import Venda


class VendaVisao(Visao):
    def __init__(self, controle: Controle, controlecliente: Controle, controleproduto: Controle):
        super().__init__(controle)
        self.controlecliente = controlecliente
        self.controleproduto = controleproduto

    def menu(self):
        top_venda = Toplevel()
        top_venda.geometry("250x200")
        top_venda.title("MENU DE VENDAS")
        venda_voltar = Button(top_venda, text="VOLTAR AO MENU INICIAL", command=top_venda.destroy).pack(ipadx=150)
        venda_ins = Button(top_venda, text="INSERIR VENDA", command=self.insercao).pack(ipadx=150)
        venda_exc = Button(top_venda, text="EXCLUIR VENDA", command=self.exclusao).pack(ipadx=150)
        venda_alt = Button(top_venda, text="ALTERAR VENDA", command=self.alteracao).pack(ipadx=150)
        venda_bID = Button(top_venda, text="BUSCAR VENDA POR ID", command=self.buscaID).pack(ipadx=150)
        venda_bVAL = Button(top_venda, text="BUSCAR VENDA POR NOME", command=self.buscaVal).pack(ipadx=150)

    def insercao(self):
        def insere():
            venda_cli_nome = texto_nome.get()
            achou_cliente = self.controlecliente.buscaVal(venda_cli_nome)
            if achou_cliente != -1:
                def addProd():
                    nome_venda = prod_nome.get()
                    buscado = self.controleproduto.buscaVal(nome_venda)
                    if buscado != -1:
                        lista_produtos.append(buscado)
                        ok_exc = Toplevel()
                        ok_exc.title("")
                        lbl_ok = Label(ok_exc, text="PRODUTO INSERIDO COM SUCESSO").pack()
                        btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
                    else:
                        ok_exc = Toplevel()
                        ok_exc.title("")
                        lbl_ok = Label(ok_exc, text="Não há produto com este nome.").pack()
                        btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()

                def finaliza():
                    venda_id = int(texto_id.get())
                    entidade = Venda(venda_id, achou_cliente, lista_produtos)
                    self.controle.insercao(entidade)
                    ok_exc = Toplevel()
                    ok_exc.title("")
                    lbl_ok = Label(ok_exc, text="VENDA INSERIDA COM SUCESSO").pack()
                    btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
                    top_insercao_produtos.destroy()
                    top_venda_insercao.destroy()

                lista_produtos = []
                top_insercao_produtos = Toplevel()
                top_insercao_produtos.title("Inserir produtos da venda")
                lbl_prod_nome = Label(top_insercao_produtos, text="DIGITE O NOME DO PRODUTO").pack()
                prod_nome = Entry(top_insercao_produtos, font=("Helvetica", 18))
                prod_nome.pack(pady=10)
                btn_confirma = Button(top_insercao_produtos, text="INSERIR PRODUTO", command=addProd).pack()
                btn_termina = Button(top_insercao_produtos, text="CADASTRAR VENDA",
                                     command=finaliza).pack()
                btn_voltar = Button(top_insercao_produtos, text="VOLTAR",
                                    command=top_insercao_produtos.destroy).pack()

            else:
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text="Não há cliente com esse nome.").pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()

        top_venda_insercao = Toplevel()
        top_venda_insercao.title("INSERIR VENDA")

        lbl_id_venda = Label(top_venda_insercao, text="DIGITE O ID DA VENDA").pack()
        texto_id = Entry(top_venda_insercao, font=("Helvetica", 18))
        texto_id.pack(pady=10)

        lbl_cli_nome = Label(top_venda_insercao, text="DIGITE O NOME DO CLIENTE").pack()
        texto_nome = Entry(top_venda_insercao, font=("Helvetica", 18))
        texto_nome.pack(pady=10)

        btn_insere = Button(top_venda_insercao, text="INSERIR VENDA", command=insere).pack()
        btn_voltar = Button(top_venda_insercao, text="VOLTAR",
                            command=top_venda_insercao.destroy).pack()

    def exclusao(self):
        def excluir():
            venda_id = int(texto_id.get())
            if self.controle.buscaID(venda_id) != -1:
                self.controle.exclusao(self.controle.buscaID(venda_id))
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text="VENDA EXCLUÍDA COM SUCESSO").pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
                top_venda_exclusao.destroy()
            else:
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text="Não há uma venda com esse ID.").pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()

        top_venda_exclusao = Toplevel()
        top_venda_exclusao.title("EXCLUIR VENDA")

        lbl_id_venda = Label(top_venda_exclusao, text="DIGITE O ID DA VENDA").pack()
        texto_id = Entry(top_venda_exclusao, font=("Helvetica", 18))
        texto_id.pack(pady=10)

        btn_insere = Button(top_venda_exclusao, text="EXCLUIR VENDA", command=excluir).pack()
        btn_voltar = Button(top_venda_exclusao, text="VOLTAR",
                            command=top_venda_exclusao.destroy).pack()

    def alteracao(self):
        def alterar():
            venda_id = int(texto_id.get())
            if self.controle.buscaID(venda_id) != -1:
                escolha = alt.get()
                if escolha == 1:
                    def alterarCliente():
                        venda_cli_nome = texto_cli.get()
                        achou_cliente = self.controlecliente.buscaVal(venda_cli_nome)
                        if achou_cliente != -1:
                            entidade = Venda(venda_id, achou_cliente, self.controle.buscaID(venda_id).lista_produto)
                            self.controle.alteracao(entidade)
                            ok_exc = Toplevel()
                            ok_exc.title("")
                            lbl_ok = Label(ok_exc, text="VENDA ALTERADA COM SUCESSO").pack()
                            btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
                            top_alt_inner.destroy()
                            top_venda_alteracao.destroy()
                        else:
                            ok_exc = Toplevel()
                            ok_exc.title("")
                            lbl_ok = Label(ok_exc, text="Não há clientes com esse nome.").pack()
                            btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()

                    top_alt_inner = Toplevel()
                    top_alt_inner.title("ALTERAR CLIENTE DA VENDA")
                    lbl_inner = Label(top_alt_inner, text="DIGITE NOVO NOME DO CLIENTE").pack()
                    texto_cli = Entry(top_alt_inner, font=("Helvetica", 18))
                    texto_cli.pack(pady=10)
                    btn_inner = Button(top_alt_inner, text="ALTERAR VENDA", command=alterarCliente).pack()
                    btn_voltarinner = Button(top_alt_inner, text="VOLTAR PARA ALTERACAO DE VENDA",
                                             command=top_alt_inner.destroy).pack()
                if escolha == 2:
                    def alterarProd():
                        nome_venda = texto_prod.get()
                        buscado = self.controleproduto.buscaVal(nome_venda)
                        if buscado != -1:
                            lista_produtos.append(buscado)
                            ok_exc = Toplevel()
                            ok_exc.title("")
                            lbl_ok = Label(ok_exc, text="PRODUTO INSERIDO COM SUCESSO").pack()
                            btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
                        else:
                            ok_exc = Toplevel()
                            ok_exc.title("")
                            lbl_ok = Label(ok_exc, text="Não há produtos com esse nome.").pack()
                            btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()

                    def finalizarAlt():
                        entidade = Venda(venda_id, self.controle.buscaID(venda_id).cliente, lista_produtos)
                        self.controle.alteracao(entidade)
                        ok_exc = Toplevel()
                        ok_exc.title("")
                        lbl_ok = Label(ok_exc, text="VENDA ALTERADA COM SUCESSO").pack()
                        btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
                        top_alt_inner2.destroy()
                        top_venda_alteracao.destroy()

                    lista_produtos = []
                    top_alt_inner2 = Toplevel()
                    top_alt_inner2.title("ALTERAR PRODUTO(S) DA VENDA")
                    lbl_inner2 = Label(top_alt_inner2, text="DIGITE O NOME DO PRODUTO").pack()
                    texto_prod = Entry(top_alt_inner2, font=("Helvetica", 18))
                    texto_prod.pack(pady=10)
                    btn_inner2 = Button(top_alt_inner2, text="ADICIONAR PRODUTO", command=alterarProd).pack()
                    btn_finalizarinner2 = Button(top_alt_inner2, text="ALTERAR VENDA",
                                                 command=finalizarAlt).pack()
                    btn_voltarinner2 = Button(top_alt_inner2, text="VOLTAR", command=top_alt_inner2.destroy).pack()
            else:
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text="Não há uma venda com esse ID.").pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()

        top_venda_alteracao = Toplevel()
        top_venda_alteracao.title("ALTERAR VENDA")

        lbl_id_venda = Label(top_venda_alteracao, text="DIGITE O ID DA VENDA").pack()
        texto_id = Entry(top_venda_alteracao, font=("Helvetica", 18))
        texto_id.pack(pady=10)

        alt = IntVar()
        Radiobutton(top_venda_alteracao, text="ALTERAR CLIENTE", variable=alt, value=1).pack()
        Radiobutton(top_venda_alteracao, text="ALTERAR PRODUTO(S)", variable=alt, value=2).pack()

        btn_altere = Button(top_venda_alteracao, text="PRÓXIMO", command=alterar).pack()
        btn_voltar = Button(top_venda_alteracao, text="VOLTAR",
                            command=top_venda_alteracao.destroy).pack()

    def buscaID(self):
        def buscar():
            venda_id = int(texto_id.get())
            if self.controle.buscaID(venda_id) != -1:
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text=self.controle.buscaID(venda_id).__str__()).pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
            else:
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text="Não há uma venda com esse ID.").pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()

        top_venda_bID = Toplevel()
        top_venda_bID.title("BUSCAR VENDA ID")

        lbl_id_venda = Label(top_venda_bID, text="DIGITE O ID DA VENDA").pack()
        texto_id = Entry(top_venda_bID, font=("Helvetica", 18))
        texto_id.pack(pady=10)

        btn_bid = Button(top_venda_bID, text="BUSCAR", command=buscar).pack()
        btn_voltar = Button(top_venda_bID, text="VOLTAR",
                            command=top_venda_bID.destroy).pack()

    def buscaVal(self):
        def buscar():
            nome_cli_venda = texto_nome.get()
            if self.controle.buscaVal(nome_cli_venda) != -1:
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text=self.controle.buscaVal(nome_cli_venda).__str__()).pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
            else:
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text="Não há uma venda com esse cliente.").pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()

        top_venda_bVal = Toplevel()
        top_venda_bVal.title("BUSCAR VENDA PELO CLIENTE")

        lbl_nome_venda = Label(top_venda_bVal, text="DIGITE O NOME DO CLIENTE DA VENDA").pack()
        texto_nome = Entry(top_venda_bVal, font=("Helvetica", 18))
        texto_nome.pack(pady=10)

        btn_bval = Button(top_venda_bVal, text="BUSCAR", command=buscar).pack()
        btn_voltar = Button(top_venda_bVal, text="VOLTAR",
                            command=top_venda_bVal.destroy).pack()
