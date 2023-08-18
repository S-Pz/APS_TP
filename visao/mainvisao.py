from tkinter import *
from visao.clivisao import ClienteVisao
from visao.prodvisao import ProdutoVisao
from visao.entrevisao import EntregaVisao
from visao.vendavisao import VendaVisao

from controle.clicont import ClienteControle
from controle.contprod import ProdutoControle
from controle.vendacont import VendaControle
from controle.entregacont import EntregaControle


class MainVisao:
    def __init__(self):
        self.produtoControle = ProdutoControle()
        self.clienteControle = ClienteControle()
        self.vendaControle = VendaControle()
        self.entregaControle = EntregaControle()

    def menu(self):
        def salvar():
            if(self.clienteControle.salvar() == False):
                print("Não foi possível salvar os clientes no arquivo.")
            if(self.produtoControle.salvar() == False):
                print("Não foi possível salvar os produtos no arquivo.")
            if(self.vendaControle.salvar() == False):
                print("Não foi possível salvar as vendas no arquivo.")
            if(self.entregaControle.salvar() == False):
                print("Não foi possível salvar as entregas no arquivo.")
            root.quit()

        if (self.clienteControle.carregar() == False):
            print("Não foi possível carregar os clientes do arquivo.")
        if (self.produtoControle.carregar() == False):
            print("Não foi possível carregar os produtos do arquivo.")
        if (self.vendaControle.carregar() == False):
            print("Não foi possível carregar as vendas do arquivo.")
        if (self.entregaControle.carregar() == False):
            print("Não foi possível carregar as entregas do arquivo.")

        root = Tk()
        root.title('MENU INICIAL - SUPERMERCADO')
        root.geometry("350x165")

        prodvis = ProdutoVisao(self.produtoControle)
        clivis = ClienteVisao(self.clienteControle)
        vendvis = VendaVisao(self.vendaControle, self.clienteControle, self.produtoControle)
        entvis = EntregaVisao(self.entregaControle, self.vendaControle)

        btn_sair = Button(root, text="SAIR DO PROGRAMA", command=salvar).pack(ipadx=150)
        btn_prod = Button(root, text="PRODUTOS", command=prodvis.menu).pack(ipadx=150)
        btn_cli  = Button(root, text="CLIENTES", command=clivis.menu).pack(ipadx=150)
        btn_ven  = Button(root, text="VENDA", command=vendvis.menu).pack(ipadx=150)
        btn_ent  = Button(root, text="ENTREGA", command=entvis.menu).pack(ipadx=150)
        root.mainloop()
