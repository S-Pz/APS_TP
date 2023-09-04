from tkinter import *
from visao.visao import Visao
from controle.controle import Controle
from modelo.pessoa import Pessoa

class PessoaVisao(Visao):
    def __init__(self, controle: Controle):
        super().__init__(controle)

    def menu(self):
        top_pessoa = Toplevel()
        top_pessoa.geometry("250x200")
        top_pessoa.title("MENU DE PESSOAS")
        pessoa_voltar = Button(top_pessoa, text="VOLTAR AO MENU INICIAL", command=top_pessoa.destroy).pack(ipadx=150)
        pessoa_gravar = Button(top_pessoa, text="INSERIR PESSOA", command=self.gravar).pack(ipadx=150)
        pessoa_apagar = Button(top_pessoa, text="EXCLUIR PESSOA", command=self.apagar).pack(ipadx=150)
        pessoa_buscar = Button(top_pessoa, text="BUSCAR PESSOA POR ID", command=self.buscar).pack(ipadx=150)

    def gravar(self):
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
                    lbl_ok = Label(ok_exc, text="PESSOA INSERIDA COM SUCESSO").pack()
                    btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
                    top_pessoa_inner.destroy()
                    top_pessoa_insercao.destroy()

                top_pessoa_inner = Toplevel()
                top_pessoa_inner.title("ENDERECO DA PESSOA")
                lbl_pessoa_inner = Label(top_pessoa_inner, text="DIGITE O ENDERECO DA PESSOA").pack()
                texto_end = Entry(top_pessoa_inner, font=("Helvetica", 18))
                texto_end.pack(pady=10)
                btn_inner = Button(top_pessoa_inner, text="INSERIR PESSOA", command=finaliza).pack()
                btn_voltar_inner = Button(top_pessoa_inner, text="VOLTAR",
                                    command=top_pessoa_inner.destroy).pack()
            else:
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text="Não há venda com esse ID.").pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
        top_pessoa_insercao = Toplevel()
        top_pessoa_insercao.title("INSERIR PESSOA")

        lbl_id_pessoa = Label(top_pessoa_insercao, text="DIGITE O ID DA PESSOA").pack()
        texto_id = Entry(top_pessoa_insercao, font=("Helvetica", 18))
        texto_id.pack(pady=10)

        lbl_id_venda = Label(top_pessoa_insercao, text="DIGITE O ID DA VENDA").pack()
        texto_venda = Entry(top_pessoa_insercao, font=("Helvetica", 18))
        texto_venda.pack(pady=10)

        btn_insere = Button(top_pessoa_insercao, text="INSERIR PESSOA", command=insere).pack()
        btn_voltar = Button(top_pessoa_insercao, text="VOLTAR",
                            command=top_pessoa_insercao.destroy).pack()

    def apagar(self):
        def exclui():
            ent_id = int(texto_id.get())
            if self.controle.buscaID(ent_id) != -1:
                self.controle.exclusao(self.controle.buscaID(ent_id))
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text="PESSOA EXCLUÍDA COM SUCESSO").pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
                top_pessoa_exclusao.destroy()
            else:
                ok_exc = Toplevel()
                ok_exc.title("")
                lbl_ok = Label(ok_exc, text="Não há pessoa com esse ID.").pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()

        top_pessoa_exclusao = Toplevel()
        top_pessoa_exclusao.title("EXCLUIR PESSOA")

        lbl_id_pessoa = Label(top_pessoa_exclusao, text="DIGITE O ID DA PESSOA").pack()
        texto_id = Entry(top_pessoa_exclusao, font=("Helvetica", 18))
        texto_id.pack(pady=10)

        btn_exclui = Button(top_pessoa_exclusao, text="INSERIR PESSOA", command=exclui).pack()
        btn_voltar = Button(top_pessoa_exclusao, text="VOLTAR",
                            command=top_pessoa_exclusao.destroy).pack()

    def buscar(self):
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
                lbl_ok = Label(ok_exc, text="Não há uma pessoa com esse ID.").pack()
                btn_ok = Button(ok_exc, text="OK", command=ok_exc.destroy).pack()
        top_ent_buscar = Toplevel()
        top_ent_buscar.title("BUSCA POR ID")

        lbl_id_ent = Label(top_ent_buscar, text="DIGITE O ID DA PESSOA").pack()
        texto_id = Entry(top_ent_buscar, font=("Helvetica", 18))
        texto_id.pack(pady=10)

        btn_busca = Button(top_ent_buscar, text="BUSCAR", command=bid).pack()
        btn_voltar = Button(top_ent_buscar, text="VOLTAR",command=top_ent_buscar.destroy).pack()
