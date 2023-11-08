from tkinter import *
from tkinter.ttk import Treeview
from customtkinter import *

from visao.visao import Visao
from controle.controle import Controle
from modelo.fornecedor import Fornecedor
from modelo.produto import Produto

class FornecedorVisao(Visao):
    def __init__(self, controle: Controle, produto_controle: Controle):
        super().__init__(controle)
        self.produto_controle = produto_controle

    def chama_menu(self, tipo_user):
        global top_fornecedor
        top_fornecedor = CTk()
        top_fornecedor.geometry("350x450")
        top_fornecedor.resizable(0, 0)
        top_fornecedor.columnconfigure(0, weight=1)
        top_fornecedor.rowconfigure(0, weight=1)
        top_fornecedor.title("MENU DE FORNECEDOR")
        self.menu(tipo_user)

    def limpa_tela(self):
        for widget in top_fornecedor.winfo_children():
            widget.grid_remove()

    def menu(self, tipo_user):
        self.limpa_tela()
        container = CTkFrame(top_fornecedor)
        container.grid(row=0, column=0)
        fornecedor_buscar = CTkButton(container, text="BUSCAR FORNECEDOR", command=lambda: self.buscar(tipo_user)).grid(pady=10, padx=10)
        if tipo_user == 2:
            fornecedor_gravar = CTkButton(container, text="INSERIR FORNECEDOR", command=self.gravar)
            fornecedor_gravar.grid(pady=10, padx=10)
            fornecedor_apagar = CTkButton(container, text="EXCLUIR FORNECEDOR", command=self.apagar)
            fornecedor_apagar.grid(pady=10, padx=10)
        fornecedor_voltar = CTkButton(container, text="VOLTAR AO MENU INICIAL", command=top_fornecedor.destroy).grid(pady=10, padx=10)

    def gravar(self):
        lista_produtos = []
        def cadastrar():
            cadastro_janela = CTkToplevel()
            label_cadastrou = CTkLabel(cadastro_janela)
            def clicou():
                o_produto = Produto(texto_nome.get(), float(texto_valor.get()), int(texto_qtd.get()), texto_cnpj.get())
                lista_produtos.append(o_produto)
                print(f"Lista de produtos: {lista_produtos}")

                texto = texto_nome.get() + " cadastrado"
                label_cadastrou = CTkLabel(cadastro_janela, text=texto)
                label_cadastrou.grid(padx=10, pady=10)
                texto_nome.delete(0, 'end')
                texto_valor.delete(0, 'end')
                texto_qtd.delete(0, 'end')

            label_nome = CTkLabel(cadastro_janela, text="DIGITE O NOME DO PRODUTO")
            label_nome.grid(row=0, column=1)
            texto_nome = CTkEntry(cadastro_janela, font=("Helvetica", 18))
            texto_nome.grid(column=1, row=1, pady=10, padx=10)

            label_valor = CTkLabel(cadastro_janela, text="DIGITE O VALOR DO PRODUTO")
            label_valor.grid(row=2, column=1)
            texto_valor = CTkEntry(cadastro_janela, font=("Helvetica", 18))
            texto_valor.grid(column=1, row=3, pady=10, padx=10)

            label_qtd = CTkLabel(cadastro_janela, text="DIGITE A QUANTIDADE FORNECIDA")
            label_qtd.grid(row=4, column=1)
            texto_qtd = CTkEntry(cadastro_janela, font=("Helvetica", 18))
            texto_qtd.grid(column=1, row=5, pady=10, padx=10)

            btn_fim = CTkButton(cadastro_janela, text="CADASTRAR", command=lambda: clicou())
            btn_fim.grid(column=1, pady=10, padx=10)

            btn_sair = CTkButton(cadastro_janela, text="SAIR", command=cadastro_janela.destroy)
            btn_sair.grid(column=1, pady=10, padx=10)

        def persistir():
            nome = texto_nome.get()
            cnpj = texto_cnpj.get()
            telefone = texto_telefone.get()
            o_fornecedor = Fornecedor(nome, cnpj, telefone)
            salvou_ou_nao = self.controle.gravar(o_fornecedor)
            
            gravou_janela = CTkToplevel()
            if salvou_ou_nao:
                for produto in lista_produtos:
                    print(f"Produto: {produto.chave}")
                    self.produto_controle.gravar(produto)
                gravou_janela.title("CADASTRO BEM SUCEDIDO")
                label_gravou = CTkLabel(gravou_janela, text="FORNECEDOR CADASTRADO COM SUCESSO").grid(pady=10, padx=10)
                btn_gravou = CTkButton(gravou_janela, text="OK", command=lambda: [self.menu(2), gravou_janela.destroy()]).grid(pady=10, padx=10)
            else:
                gravou_janela.title("CADASTRO NÃO REALIZADO")
                label_nao_gravou = CTkLabel(gravou_janela, text="NÃO FOI POSSÍVEL CADASTRAR O FORNECEDOR\nREVISE OS DADOS").grid(pady=10, padx=10)
                btn_gravou = CTkButton(gravou_janela, text="OK", command=gravou_janela.destroy).grid(pady=10, padx=10)

        self.limpa_tela()
        container = CTkFrame(top_fornecedor)
        container.grid(pady=10, padx=10)

        label_nome_fornecedor = CTkLabel(container, text="DIGITE O NOME DO FORNECEDOR")
        label_nome_fornecedor.grid(row=0, column=1)
        texto_nome = CTkEntry(container, font=("Helvetica", 18))
        texto_nome.grid(column=1, row=1, pady=10, padx=10)

        label_telefone_fornecedor = CTkLabel(container, text="DIGITE O TELEFONE DO FORNECEDOR")
        label_telefone_fornecedor.grid(row=2, column=1)
        texto_telefone = CTkEntry(container, font=("Helvetica", 18))
        texto_telefone.grid(column=1, row=3, pady=10, padx=10)

        label_cnpj_fornecedor = CTkLabel(container, text="DIGITE O CNPJ DO FORNECEDOR")
        label_cnpj_fornecedor.grid(row=4, column=1)
        texto_cnpj = CTkEntry(container, font=("Helvetica", 18))
        texto_cnpj.grid(column=1, row=5,pady=10, padx=10)

        label_produto_fornecedor = CTkButton(container, text="CADASTRAR PRODUTOS", command=cadastrar)
        label_produto_fornecedor.grid(row=6, column=1)

        btn_finalizar = CTkButton(container, text="FINALIZAR", command=persistir)
        btn_finalizar.grid(column=1, row=7, pady=10, padx=10)
        btn_voltar = CTkButton(container, text="VOLTAR", command= top_fornecedor.destroy)
        btn_voltar.grid(column=1, pady=10, padx=10)

    def apagar(self):
        def excluir():
            fornecedor_id = texto_id.get()
            if self.controle.apagar(fornecedor_id):
                ok_exc = CTkToplevel()
                ok_exc.title("")
                lbl_ok = CTkLabel(ok_exc, text="FORNECEDOR EXCLUÍDO COM SUCESSO").grid(pady=10, padx=10)
                btn_ok = CTkButton(ok_exc, text="OK", command=ok_exc.destroy).grid(pady=10, padx=10)
            else:
                ok_exc = CTkToplevel()
                ok_exc.title("")
                lbl_ok = CTkLabel(ok_exc, text="Não há esse fornecedor no banco.").grid(pady=10, padx=10)
                btn_ok = CTkButton(ok_exc, text="OK", command=ok_exc.destroy).grid(pady=10, padx=10)

        self.limpa_tela()
        top_fornecedor_exclusao = CTkFrame(top_fornecedor)
        top_fornecedor_exclusao.grid(pady=10, padx=10)

        lbl_id_fornecedor = CTkLabel(top_fornecedor_exclusao, text="DIGITE O CNPJ DO FORNECEDOR").grid(pady=10, padx=10)
        texto_id = CTkEntry(top_fornecedor_exclusao, font=("Helvetica", 18))
        texto_id.grid(pady=10)

        btn_insere = CTkButton(top_fornecedor_exclusao, text="EXCLUIR FORNECEDOR", command=excluir).grid(pady=10, padx=10)
        btn_voltar = CTkButton(top_fornecedor_exclusao, text="VOLTAR",
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

            resultado['columns'] = ('nome', 'cnpj', 'telefone')
            resultado.column("#0", width=0,  stretch=YES)
            resultado.column("nome",anchor=CENTER, width=80)
            resultado.column("cnpj",anchor=CENTER,width=80)
            resultado.column("telefone",anchor=CENTER,width=80)

            resultado.heading("#0",text="",anchor=CENTER)
            resultado.heading("nome",text="Nome",anchor=CENTER)
            resultado.heading("cnpj",text="CNPJ",anchor=CENTER)
            resultado.heading("telefone",text="Telefone",anchor=CENTER)

            for (indice, fornecedor) in enumerate(achados):
                resultado.insert(parent='',index='end',iid=indice,text='',
                                 values=(fornecedor[0],fornecedor[1], fornecedor[2]))

            lbl_janela = CTkLabel(janela_achados, text="RESULTADO DA PESQUISA").pack(pady=10, padx=10)

            btn_ok = CTkButton(janela_achados, text="OK", command=janela_achados.destroy).pack(pady=10, padx=10)

        self.limpa_tela()
        top_fornecedor_buscar = CTkFrame(top_fornecedor)
        top_fornecedor_buscar.grid(pady=10, padx=10)

        lbl_id_fornecedor = CTkLabel(top_fornecedor_buscar, text="DIGITE O NOME DO FORNECEDOR").grid(pady=10, padx=10)
        texto_id = CTkEntry(top_fornecedor_buscar, font=("Helvetica", 18))
        texto_id.grid(pady=10)

        btn_buscar = CTkButton(top_fornecedor_buscar, text="BUSCAR", command=procura)
        btn_buscar.grid(pady=10, padx=10)
        btn_voltar = CTkButton(top_fornecedor_buscar, text="VOLTAR", command=lambda: self.menu(tipo_user))
        btn_voltar.grid(pady=10, padx=10)

