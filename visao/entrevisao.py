from tkinter import *
from visao.visao import Visao
from controle.controle import Controle
from modelo.entrega import Entrega


class EntregaVisao(Visao):
    def __init__(self, controle: Controle, controlevenda: Controle):
        super().__init__(controle)
        self.controlevenda = controlevenda

    def menu(self):
        top_entrega = Toplevel()
        top_entrega.geometry("250x200")
        top_entrega.title("MENU DE ENTREGAS")
        entrega_voltar = Button(top_entrega, text="VOLTAR AO MENU INICIAL", command=top_entrega.destroy).pack(ipadx=150)
        entrega_ins = Button(top_entrega, text="INSERIR ENTREGA", command=self.insercao).pack(ipadx=150)
        entrega_exc = Button(top_entrega, text="EXCLUIR ENTREGA", command=self.exclusao).pack(ipadx=150)
        entrega_alt = Button(top_entrega, text="ALTERAR ENTREGA", command=self.alteracao).pack(ipadx=150)
        entrega_bID = Button(top_entrega, text="BUSCAR ENTREGA POR ID", command=self.buscaID).pack(ipadx=150)
        entrega_bVAL = Button(top_entrega, text="BUSCAR ENTREGA POR NOME", command=self.buscaVal).pack(ipadx=150)

    def insercao(self):
        def insere():
            venda_id = int(texto_venda.get())
            ent_id = int(texto_id.get())
            if self.controlevenda.buscaID(venda_id) != -1:
                venda = self.controlevenda.buscaID(venda_id)
                def finaliza():
                    ent_end = texto_end.get()
                    entidade = Entrega(ent_id, venda, ent_end)
                    self.controle.insercao(entidade)
                    ok_exc = Toplevel()
                    ok_exc.title("")
                    lbl_ok = Label(ok_exc, text="ENTREGA INSERIDA COM SUCESSO").pack()
                    btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
                    top_entrega_inner.destroy()
                    top_entrega_insercao.destroy()

                top_entrega_inner = Toplevel()
                top_entrega_inner.title("ENDERECO DA ENTREGA")
                lbl_entrega_inner = Label(top_entrega_inner, text="DIGITE O ENDERECO DA ENTREGA").pack()
                texto_end = Entry(top_entrega_inner, font=("Helvetica", 18))
                texto_end.pack(pady=10)
                btn_inner = Button(top_entrega_inner, text="INSERIR ENTREGA", command=finaliza).pack()
                btn_voltar_inner = Button(top_entrega_inner, text="VOLTAR",
                                    command=top_entrega_inner.destroy).pack()
            else:
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text="Não há venda com esse ID.").pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
        top_entrega_insercao = Toplevel()
        top_entrega_insercao.title("INSERIR ENTREGA")

        lbl_id_entrega = Label(top_entrega_insercao, text="DIGITE O ID DA ENTREGA").pack()
        texto_id = Entry(top_entrega_insercao, font=("Helvetica", 18))
        texto_id.pack(pady=10)

        lbl_id_venda = Label(top_entrega_insercao, text="DIGITE O ID DA VENDA").pack()
        texto_venda = Entry(top_entrega_insercao, font=("Helvetica", 18))
        texto_venda.pack(pady=10)

        btn_insere = Button(top_entrega_insercao, text="INSERIR ENTREGA", command=insere).pack()
        btn_voltar = Button(top_entrega_insercao, text="VOLTAR",
                            command=top_entrega_insercao.destroy).pack()

    def exclusao(self):
        def exclui():
            ent_id = int(texto_id.get())
            if self.controle.buscaID(ent_id) != -1:
                self.controle.exclusao(self.controle.buscaID(ent_id))
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text="ENTREGA EXCLUÍDA COM SUCESSO").pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
                top_entrega_exclusao.destroy()
            else:
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text="Não há entrega com esse ID.").pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()

        top_entrega_exclusao = Toplevel()
        top_entrega_exclusao.title("EXCLUIR ENTREGA")

        lbl_id_entrega = Label(top_entrega_exclusao, text="DIGITE O ID DA ENTREGA").pack()
        texto_id = Entry(top_entrega_exclusao, font=("Helvetica", 18))
        texto_id.pack(pady=10)

        btn_exclui = Button(top_entrega_exclusao, text="INSERIR ENTREGA", command=exclui).pack()
        btn_voltar = Button(top_entrega_exclusao, text="VOLTAR",
                            command=top_entrega_exclusao.destroy).pack()

    def alteracao(self):
        def alterar():
            ent_id = int(texto_id.get())
            achou_ent = self.controle.buscaID(ent_id)
            if achou_ent != -1:
                escolha = alt.get()
                if escolha == 1:
                    def altereinner():
                        novoid = int(texto_id_venda.get())
                        novavenda = self.controlevenda.buscaID(novoid)
                        entidade = Entrega(ent_id, novavenda, achou_ent.endereco)
                        self.controle.alteracao(entidade)
                        ok_exc = Toplevel()
                        ok_exc.title("")
                        lbl_ok = Label(ok_exc, text="ENTREGA ALTERADA COM SUCESSO").pack()
                        btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
                        top_entrega_inner.destroy()
                        top_entrega_alteracao.destroy()
                    top_entrega_inner = Toplevel()
                    top_entrega_inner.title("ALTERAR ENTREGA")
                    lbl_entrega_inner = Label(top_entrega_inner, text="DIGITE O ID DA NOVA ENTREGA").pack()
                    texto_id_venda = Entry(top_entrega_inner, font=("Helvetica", 18))
                    texto_id_venda.pack(pady=10)
                    btn_inner = Button(top_entrega_inner, text="ALTERAR ENTREGA", command=altereinner).pack()
                    btn_voltar_inner = Button(top_entrega_inner, text="VOLTAR",
                                              command=top_entrega_inner.destroy).pack()
                if escolha == 2:
                    def altereinner2():
                        novoend = texto_end.get()
                        entidade = Entrega(ent_id, achou_ent.venda, novoend)
                        self.controle.alteracao(entidade)
                        ok_exc = Toplevel()
                        ok_exc.title("")
                        lbl_ok = Label(ok_exc, text="ENDEREÇO ALTERADO COM SUCESSO").pack()
                        btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
                        top_entrega_inner2.destroy()
                        top_entrega_alteracao.destroy()
                    top_entrega_inner2 = Toplevel()
                    top_entrega_inner2.title("ALTERAR ENTREGA")
                    lbl_entrega_inner2 = Label(top_entrega_inner2, text="DIGITE O NOVO ENDERECO").pack()
                    texto_end = Entry(top_entrega_inner2, font=("Helvetica", 18))
                    texto_end.pack(pady=10)
                    btn_inner2 = Button(top_entrega_inner2, text="ALTERAR ENTREGA", command=altereinner2).pack()
                    btn_voltar_inner2 = Button(top_entrega_inner2, text="VOLTAR",
                                              command=top_entrega_inner2.destroy).pack()
            else:
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text="Não há uma entrega com esse ID.").pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
        top_entrega_alteracao = Toplevel()
        top_entrega_alteracao.title("ALTERAR ENTREGA")

        lbl_id_ent = Label(top_entrega_alteracao, text="DIGITE O ID DA ENTREGA").pack()
        texto_id = Entry(top_entrega_alteracao, font=("Helvetica", 18))
        texto_id.pack(pady=10)

        alt = IntVar()
        Radiobutton(top_entrega_alteracao, text="ALTERAR VENDA", variable=alt, value=1).pack()
        Radiobutton(top_entrega_alteracao, text="ALTERAR ENDERECO", variable=alt, value=2).pack()

        btn_alterar = Button(top_entrega_alteracao, text="ALTERAR ENTREGA", command=alterar).pack()
        btn_voltar = Button(top_entrega_alteracao, text="VOLTAR",command=top_entrega_alteracao.destroy).pack()

    def buscaID(self):
        def bid():
            ent_id = int(texto_id.get())
            if self.controle.buscaID(ent_id) != -1:
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text=self.controle.buscaID(ent_id).__str__()).pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
            else:
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text="Não há uma entrega com esse ID.").pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
        top_ent_bID = Toplevel()
        top_ent_bID.title("BUSCA POR ID")

        lbl_id_ent = Label(top_ent_bID, text="DIGITE O ID DA ENTREGA").pack()
        texto_id = Entry(top_ent_bID, font=("Helvetica", 18))
        texto_id.pack(pady=10)

        btn_busca = Button(top_ent_bID, text="BUSCAR", command=bid).pack()
        btn_voltar = Button(top_ent_bID, text="VOLTAR",command=top_ent_bID.destroy).pack()
        
    def buscaVal(self):
        def bval():
            ent_val = texto_nome.get()
            if self.controle.buscaVal(ent_val) != -1:
                print(self.controle.buscaVal(ent_val).__str__())
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text=self.controle.buscaVal(ent_val).__str__()).pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
            else:
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text="Entrega não encontrada.").pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
        top_ent_bVal = Toplevel()
        top_ent_bVal.title("BUSCA POR CLIENTE")

        lbl_id_ent = Label(top_ent_bVal, text="DIGITE O CLIENTE DA ENTREGA").pack()
        texto_nome = Entry(top_ent_bVal, font=("Helvetica", 18))
        texto_nome.pack(pady=10)

        btn_busca = Button(top_ent_bVal, text="BUSCAR", command=bval).pack()
        btn_voltar = Button(top_ent_bVal, text="VOLTAR", command=top_ent_bVal.destroy).pack()