from tkinter import *
<<<<<<< HEAD
from tkinter.ttk import Treeview
from customtkinter import *

=======
>>>>>>> origin/main
from visao.visao import Visao
from controle.controle import Controle
from modelo.patrocinador import Patrocinador

class PatrocinadorVisao(Visao):
    def __init__(self, controle: Controle):
        super().__init__(controle)

<<<<<<< HEAD
    def chama_menu(self, tipo_user):
        global top_patrocinador
        top_patrocinador = CTk()
        top_patrocinador.geometry("350x450")
        top_patrocinador.resizable(0, 0)
        top_patrocinador.columnconfigure(0, weight=1)
        top_patrocinador.rowconfigure(0, weight=1)
        top_patrocinador.title("MENU DE PATROCINADOR")
        self.menu(tipo_user)

    def limpa_tela(self):
        for widget in top_patrocinador.winfo_children():
            widget.grid_remove()

    def menu(self, tipo_user):
        self.limpa_tela()
        container = CTkFrame(top_patrocinador)
        container.grid(row=0, column=0)
        patrocinador_buscar = CTkButton(container, text="BUSCAR PATROCINADOR", command=lambda: self.buscar(tipo_user)).grid(pady=10, padx=10)
        if tipo_user == 2:
            patrocinador_gravar = CTkButton(container, text="INSERIR PATROCINADOR", command=self.gravar)
            patrocinador_gravar.grid(pady=10, padx=10)
            patrocinador_apagar = CTkButton(container, text="EXCLUIR PATROCINADOR", command=self.apagar)
            patrocinador_apagar.grid(pady=10, padx=10)
        patrocinador_voltar = CTkButton(container, text="VOLTAR AO MENU INICIAL", command=top_patrocinador.destroy).grid(pady=10, padx=10)

    def gravar(self):
        def persistir():
            nome = texto_nome.get()
            cnpj = texto_cnpj.get()
            valor_contrato = float( texto_valor.get() )
            telefone = texto_telefone.get()
            local_merchan = texto_local.get()
            o_patrocinador = Patrocinador(nome, cnpj, telefone, valor_contrato, local_merchan)
            salvou_ou_nao = self.controle.gravar(o_patrocinador)
            gravou_janela = CTkToplevel()
            if salvou_ou_nao:
                gravou_janela.title("CADASTRO BEM SUCEDIDO")
                label_gravou = CTkLabel(gravou_janela, text="PATROCINADOR CADASTRADO COM SUCESSO").grid(pady=10, padx=10)
                btn_gravou = CTkButton(gravou_janela, text="OK", command=lambda: [self.menu(2), gravou_janela.destroy()]).grid(pady=10, padx=10)
            else:
                gravou_janela.title("CADASTRO NÃO REALIZADO")
                label_nao_gravou = CTkLabel(gravou_janela, text="NÃO FOI POSSÍVEL CADASTRAR O PATROCINADOR\nREVISE OS DADOS").grid(pady=10, padx=10)
                btn_gravou = CTkButton(gravou_janela, text="OK", command=gravou_janela.destroy).grid(pady=10, padx=10)

        self.limpa_tela()
        container = CTkFrame(top_patrocinador)
        container.grid(pady=10, padx=10)

        label_nome_patrocinador = CTkLabel(container, text="DIGITE O NOME DO PATROCINADOR")
        label_nome_patrocinador.grid(row=0, column=1)
        texto_nome = CTkEntry(container, font=("Helvetica", 18))
        texto_nome.grid(column=1, row=1, pady=10, padx=10)

        label_telefone_patrocinador = CTkLabel(container, text="DIGITE O TELEFONE DO PATROCINADOR")
        label_telefone_patrocinador.grid(row=2, column=1)
        texto_telefone = CTkEntry(container, font=("Helvetica", 18))
        texto_telefone.grid(column=1, row=3, pady=10, padx=10)

        label_cnpj_patrocinador = CTkLabel(container, text="DIGITE O CNPJ DO PATROCINADOR")
        label_cnpj_patrocinador.grid(row=4, column=1)
        texto_cnpj = CTkEntry(container, font=("Helvetica", 18))
        texto_cnpj.grid(column=1, row=5,pady=10, padx=10)

        label_valor_patrocinador = CTkLabel(container, text="DIGITE O VALOR DO CONTRATO")
        label_valor_patrocinador.grid(row=6, column=1)
        texto_valor = CTkEntry(container)
        texto_valor.grid(column=1,row=7,pady=10)

        label_local_patrocinador = CTkLabel(container, text="DIGITE O LOCAL DO MERCHANDISING")
        label_local_patrocinador.grid(row=8, column=1)
        texto_local = CTkEntry(container)
        texto_local.grid(column=1,row=9,pady=10)

        btn_finalizar = CTkButton(container, text="FINALIZAR", command=persistir)
        btn_finalizar.grid(column=1, pady=10, padx=10)
        btn_voltar = CTkButton(container, text="VOLTAR", command=lambda: self.menu(2))
        btn_voltar.grid(column=1, pady=10, padx=10)

    def apagar(self):
        def excluir():
            patrocinador_id = texto_id.get()
            if self.controle.apagar(patrocinador_id):
                ok_exc = CTkToplevel()
                ok_exc.title("")
                lbl_ok = CTkLabel(ok_exc, text="PATROCINADOR EXCLUÍDO COM SUCESSO").grid(pady=10, padx=10)
                btn_ok = CTkButton(ok_exc, text="OK", command=lambda: [self.menu(2), ok_exc.destroy()]).grid(pady=10, padx=10)
            else:
                ok_exc = CTkToplevel()
                ok_exc.title("")
                lbl_ok = CTkLabel(ok_exc, text="Não há esse patrocinador no banco.").grid(pady=10, padx=10)
                btn_ok = CTkButton(ok_exc, text="OK", command=ok_exc.destroy).grid(pady=10, padx=10)

        self.limpa_tela()
        top_patrocinador_exclusao = CTkFrame(top_patrocinador)
        top_patrocinador_exclusao.grid(pady=10, padx=10)

        lbl_id_patrocinador = CTkLabel(top_patrocinador_exclusao, text="DIGITE O CNPJ DO PATROCINADOR").grid(pady=10, padx=10)
        texto_id = CTkEntry(top_patrocinador_exclusao, font=("Helvetica", 18))
        texto_id.grid(pady=10)

        btn_insere = CTkButton(top_patrocinador_exclusao, text="EXCLUIR PATROCINADOR", command=excluir).grid(pady=10, padx=10)
        btn_voltar = CTkButton(top_patrocinador_exclusao, text="VOLTAR",
                               command=lambda: self.menu(2)).grid(pady=10, padx=10)

    def buscar(self, tipo_user):
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

            resultado['columns'] = ('nome', 'cnpj', 'telefone', 'valor_contrato', 'local_merchan')
            resultado.column("#0", width=0,  stretch=NO)
            resultado.column("nome",anchor=CENTER, width=80)
            resultado.column("cnpj",anchor=CENTER,width=80)
            resultado.column("telefone",anchor=CENTER,width=80)
            resultado.column("valor_contrato",anchor=CENTER,width=80)
            resultado.column("local_merchan",anchor=CENTER,width=80)

            resultado.heading("#0",text="",anchor=CENTER)
            resultado.heading("nome",text="Nome",anchor=CENTER)
            resultado.heading("cnpj",text="CNPJ",anchor=CENTER)
            resultado.heading("telefone",text="Telefone",anchor=CENTER)
            resultado.heading("valor_contrato",text="Valor do Contrato (R$)",anchor=CENTER)
            resultado.heading("local_merchan",text="Local do Merchan",anchor=CENTER)

            for (indice, patrocinador) in enumerate(achados):
                resultado.insert(parent='',index='end',iid=indice,text='',
                                 values=(patrocinador[0],patrocinador[1], patrocinador[2], patrocinador[3], patrocinador[4]))

            lbl_janela = CTkLabel(janela_achados, text="RESULTADO DA PESQUISA").pack(pady=10, padx=10)

            btn_ok = CTkButton(janela_achados, text="OK", command=janela_achados.destroy).pack(pady=10, padx=10)

        self.limpa_tela()
        top_patrocinador_buscar = CTkFrame(top_patrocinador)
        top_patrocinador_buscar.grid(pady=10, padx=10)

        lbl_id_patrocinador = CTkLabel(top_patrocinador_buscar, text="DIGITE O NOME DO PATROCINADOR").grid(pady=10, padx=10)
        texto_id = CTkEntry(top_patrocinador_buscar, font=("Helvetica", 18))
        texto_id.grid(pady=10)

        btn_buscar = CTkButton(top_patrocinador_buscar, text="BUSCAR", command=procura)
        btn_buscar.grid(pady=10, padx=10)
        btn_voltar = CTkButton(top_patrocinador_buscar, text="VOLTAR", command=lambda: self.menu(tipo_user))
        btn_voltar.grid(pady=10, padx=10)
=======
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

    def gravar(self):
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

    def apagar(self):
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

    def buscar(self):
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
>>>>>>> origin/main
