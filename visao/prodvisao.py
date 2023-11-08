from tkinter import *
from visao.visao import Visao
from controle.controle import Controle
from modelo.produto import Produto


class ProdutoVisao(Visao):
    def __init__(self, controle: Controle):
        super().__init__(controle)

    def menu(self):
        top_prod = Toplevel()
        top_prod.geometry("250x200")
        top_prod.title("MENU DE PRODUTOS")
        prod_voltar = Button(top_prod, text="VOLTAR AO MENU INICIAL", command=top_prod.destroy).pack(ipadx=150)
        prod_ins = Button(top_prod, text="INSERIR PRODUTO", command=self.insercao).pack(ipadx=150)
        prod_exc = Button(top_prod, text="EXCLUIR PRODUTO", command=self.exclusao).pack(ipadx=150)
        prod_alt = Button(top_prod, text="ALTERAR PRODUTO", command=self.alteracao).pack(ipadx=150)
        prod_bID = Button(top_prod, text="BUSCAR PRODUTO POR ID", command=self.buscaID).pack(ipadx=150)
        prod_bVAL = Button(top_prod, text="BUSCAR PRODUTO POR NOME", command=self.buscaVal).pack(ipadx=150)

    def insercao(self):  # virar Entry
        def insere():
            prod_id = int(texto_id.get())
            prod_nome = texto_nome.get()
            prod_valor = float(texto_valor.get())
            entidade = Produto(prod_id, prod_valor, prod_nome)
            self.controle.insercao(entidade)
            ok_exc = Toplevel()
            ok_exc.title("")
            lbl_ok = Label(ok_exc, text="PRODUTO INSERIDO COM SUCESSO").pack()
            btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
            top_prod_insercao.destroy()

        top_prod_insercao = Toplevel()
        top_prod_insercao.title("INSERIR PRODUTO")

        lbl_id_prod = Label(top_prod_insercao, text="DIGITE O ID DO PRODUTO").pack()
        texto_id = Entry(top_prod_insercao, font=("Helvetica", 18))
        texto_id.pack(pady=10)

        lbl_prod_nome = Label(top_prod_insercao, text="DIGITE O NOME DO PRODUTO").pack()
        texto_nome = Entry(top_prod_insercao, font=("Helvetica", 18))
        texto_nome.pack(pady=10)

        lbl_prod_valor = Label(top_prod_insercao, text="DIGITE O VALOR DO PRODUTO").pack()
        texto_valor = Entry(top_prod_insercao, font=("Helvetica", 18))
        texto_valor.pack(pady=10)

        btn_insere = Button(top_prod_insercao, text="INSERIR PRODUTO", command=insere).pack()
        btn_voltar = Button(top_prod_insercao, text="VOLTAR", command=top_prod_insercao.destroy).pack()

    def exclusao(self):  # virar Entry
        def exclui():
            prod_id = int(texto_id.get())
            if self.controle.buscaID(prod_id) != -1:
                self.controle.exclusao(self.controle.buscaID(prod_id))
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text="PRODUTO EXCLUÍDO COM SUCESSO").pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
                top_prod_exclusao.destroy()
            else:
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text="Não há um produto com esse ID.").pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
        top_prod_exclusao = Toplevel()
        top_prod_exclusao.title("EXCLUIR PRODUTO")

        lbl_id_prod = Label(top_prod_exclusao, text="DIGITE O ID DO PRODUTO").pack()
        texto_id = Entry(top_prod_exclusao, font=("Helvetica", 18))
        texto_id.pack(pady=10)

        btn_insere = Button(top_prod_exclusao, text="EXCLUIR PRODUTO", command=exclui).pack()
        btn_voltar = Button(top_prod_exclusao, text="VOLTAR",command=top_prod_exclusao.destroy).pack()

    def alteracao(self):
        def alterar():
            prod_id = int(texto_id.get())
            achou_prod = self.controle.buscaID(prod_id)
            if achou_prod != -1:
                escolha = alt.get()
                if escolha == 1:
                    def alt_in():
                        alterado = novo_nome.get()
                        entidade = Produto(prod_id, achou_prod.preco, alterado)
                        self.controle.alteracao(entidade)
                        ok_exc = Toplevel()
                        ok_exc.title("")
                        lbl_ok = Label(ok_exc, text="Nome do produto alterado com sucesso.").pack()
                        btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
                        top_alt_nome.destroy()
                        top_prod_alteracao.destroy()

                    top_alt_nome = Toplevel()
                    top_alt_nome.title("ALTERAÇÃO DE NOME")
                    lbl_novo_nome = Label(top_alt_nome, text="DIGITE O NOVO NOME").pack()
                    novo_nome = Entry(top_alt_nome, font=("Helvetica", 18))
                    novo_nome.pack(pady=10)
                    btn_voltar = Button(top_alt_nome, text="ALTERAR NOME",
                                        command=alt_in).pack()

                if escolha == 2:
                    def alt_in():
                        alterado = float(novo_preco.get())
                        entidade = Produto(prod_id, alterado, achou_prod.nome)
                        self.controle.alteracao(entidade)
                        ok_exc = Toplevel()
                        ok_exc.title("")
                        lbl_ok = Label(ok_exc, text="Preço do produto alterado com sucesso.").pack()
                        btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
                        top_alt_preco.destroy()
                        top_prod_alteracao.destroy()

                    top_alt_preco = Toplevel()
                    top_alt_preco.title("ALTERAÇÃO DE PREÇO")
                    lbl_novo_preco = Label(top_alt_preco, text="DIGITE O NOVO PREÇO").pack()
                    novo_preco = Entry(top_alt_preco, font=("Helvetica", 18))
                    novo_preco.pack(pady=10)
                    btn_voltar = Button(top_alt_preco, text="ALTERAR PREÇO",
                                        command=alt_in).pack()
            else:
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text="Não há um produto com esse ID.").pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()

        top_prod_alteracao = Toplevel()
        top_prod_alteracao.title("ALTERAR PRODUTO")

        lbl_id_prod = Label(top_prod_alteracao, text="DIGITE O ID DO PRODUTO").pack()
        texto_id = Entry(top_prod_alteracao, font=("Helvetica", 18))
        texto_id.pack(pady=10)

        alt = IntVar()
        Radiobutton(top_prod_alteracao, text="ALTERAR NOME", variable=alt, value=1).pack()
        Radiobutton(top_prod_alteracao, text="ALTERAR PREÇO", variable=alt, value=2).pack()

        btn_alterar = Button(top_prod_alteracao, text="ALTERAR PRODUTO", command=alterar).pack()
        btn_voltar = Button(top_prod_alteracao, text="VOLTAR",command=top_prod_alteracao.destroy).pack()

    def buscaID(self):
        def bid():
            prod_id = int(texto_id.get())
            if self.controle.buscaID(prod_id) != -1:
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text=self.controle.buscaID(prod_id).__str__()).pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
            else:
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text="Não há um produto com esse ID.").pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
        top_prod_bID = Toplevel()
        top_prod_bID.title("BUSCA POR ID")

        lbl_id_prod = Label(top_prod_bID, text="DIGITE O ID DO PRODUTO").pack()
        texto_id = Entry(top_prod_bID, font=("Helvetica", 18))
        texto_id.pack(pady=10)

        btn_insere = Button(top_prod_bID, text="BUSCAR", command=bid).pack()
        btn_voltar = Button(top_prod_bID, text="VOLTAR",command=top_prod_bID.destroy).pack()

    def buscaVal(self):
        def bval():
            prod_Val = texto_val.get()
            if self.controle.buscaVal(prod_Val) != -1:
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text=self.controle.buscaVal(prod_Val).__str__()).pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
            else:
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text="Não há um produto com esse nome.").pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()

        top_prod_bVal = Toplevel()
        top_prod_bVal.title("BUSCA POR NOME")

        lbl_id_prod = Label(top_prod_bVal, text="DIGITE O NOME DO PRODUTO").pack()
        texto_val = Entry(top_prod_bVal, font=("Helvetica", 18))
        texto_val.pack(pady=10)

        btn_insere = Button(top_prod_bVal, text="BUSCAR", command=bval).pack()
        btn_voltar = Button(top_prod_bVal, text="VOLTAR", command=top_prod_bVal.destroy).pack()
