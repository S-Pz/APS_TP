from tkinter.ttk import Treeview
from customtkinter import *

from visao.visao import Visao
from visao.usuario_visao import UsuarioVisao
from controle.controle import Controle
from modelo.pessoa import Pessoa

class PessoaVisao(Visao):
    def __init__(self, controle: Controle):
        super().__init__(controle)

    def chama_menu(self, tipo_user):
        global top_pessoa
        top_pessoa = CTk()
        top_pessoa.geometry("350x450")
        top_pessoa.resizable(0, 0)
        top_pessoa.columnconfigure(0, weight=1)
        top_pessoa.rowconfigure(0, weight=1)
        top_pessoa.title("MENU DE PESSOA")
        self.menu(tipo_user)

    def limpa_tela(self):
        for widget in top_pessoa.winfo_children():
            widget.grid_remove()

    def menu(self, tipo_user: int):
        self.limpa_tela()
        container = CTkFrame(top_pessoa)
        container.grid(row=0, column=0)
        pessoa_buscar = CTkButton(container, text="BUSCAR PESSOA", command=lambda: self.buscar(tipo_user)).grid(pady=10, padx=10)
        if tipo_user == 2:
            #pessoa_gravar = CTkButton(container, text="INSERIR PESSOA", command=lambda: self.gravar(usuario_visao))
            #pessoa_gravar.grid(pady=10, padx=10)
            pessoa_apagar = CTkButton(container, text="EXCLUIR PESSOA", command=self.apagar)
            pessoa_apagar.grid(pady=10, padx=10)
        pessoa_voltar = CTkButton(container, text="VOLTAR AO MENU INICIAL", command=top_pessoa.destroy).grid(pady=10, padx=10)

    def gravar(self, usuario_visao):
        def cadastro_user(nome):
            usuario_visao.gravar(nome)

        def persistir():
            nome = texto_nome.get()
            cpf = texto_cpf.get()
            data = f"{texto_ano.get()}-{texto_mes.get()}-{texto_dia.get()}"
            salario = float( texto_salario.get() )
            telefone = texto_telefone.get()
            funcao = texto_funcao.get()
            o_pessoa = Pessoa(nome, cpf, data, salario, telefone, funcao)
            salvou_ou_nao = self.controle.gravar(o_pessoa)
            gravou_janela = CTkToplevel()
            if salvou_ou_nao:
                gravou_janela.title("CADASTRO BEM SUCEDIDO")
                label_gravou = CTkLabel(gravou_janela, text="PESSOA CADASTRADA COM SUCESSO").grid(pady=10, padx=10)
                btn_gravou = CTkButton(gravou_janela, text="OK", command=lambda: [cadastro_user(nome), top_pessoa_gravar.destroy(), gravou_janela.destroy()]).grid(pady=10, padx=10)
            else:
                gravou_janela.title("CADASTRO NÃO REALIZADO")
                label_nao_gravou = CTkLabel(gravou_janela, text="NÃO FOI POSSÍVEL CADASTRAR A PESSOA\nREVISE OS DADOS").grid(pady=10, padx=10)
                btn_gravou = CTkButton(gravou_janela, text="OK", command=gravou_janela.destroy).grid(pady=10, padx=10)

        top_pessoa_gravar = CTkToplevel()
        top_pessoa_gravar.geometry("800x800")
        top_pessoa_gravar.columnconfigure(0, weight=1)
        top_pessoa_gravar.rowconfigure(0, weight=1)
        top_pessoa_gravar.title("MENU DE CADASTRO")

        container = CTkFrame(top_pessoa_gravar)
        container.grid(pady=10, padx=10)

        label_nome_pessoa = CTkLabel(container, text="DIGITE O NOME DA PESSOA")
        label_nome_pessoa.grid(row=0, column=1)
        texto_nome = CTkEntry(container, font=("Helvetica", 18))
        texto_nome.grid(column=1, row=1, pady=10, padx=10)

        label_cpf_pessoa = CTkLabel(container, text="DIGITE O CPF DA PESSOA")
        label_cpf_pessoa.grid(row=2, column=1)
        texto_cpf = CTkEntry(container, font=("Helvetica", 18))
        texto_cpf.grid(column=1, row=3,pady=10, padx=10)

        label_data_pessoa = CTkLabel(container, text="DIGITE A DATA DE NASCIMENTO DA PESSOA")
        label_data_pessoa.grid(row=4, column=1)
        texto_dia = CTkEntry(container)
        texto_dia.grid(column=0, row=5, pady=10, padx=10)
        texto_mes = CTkEntry(container)
        texto_mes.grid(column=1, row=5, pady=10, padx=10)
        texto_ano = CTkEntry(container)
        texto_ano.grid(column=2, row=5, pady=10, padx=10)

        label_salario_pessoa = CTkLabel(container, text="DIGITE O SALARIO DA PESSOA")
        label_salario_pessoa.grid(row=6, column=1)
        texto_salario = CTkEntry(container)
        texto_salario.grid(column=1,row=7,pady=10, padx=10)
    
        label_telefone_pessoa = CTkLabel(container, text="DIGITE O TELEFONE DA PESSOA")
        label_telefone_pessoa.grid(row=8, column=1)
        texto_telefone = CTkEntry(container)
        texto_telefone.grid(column=1,row=9,pady=10)

        label_funcao_pessoa = CTkLabel(container, text="DIGITE A FUNÇÃO DA PESSOA")
        label_funcao_pessoa.grid(row=10, column=1)
        texto_funcao = CTkEntry(container)
        texto_funcao.grid(column=1,row=11,pady=10)

        btn_finalizar = CTkButton(container, text="FINALIZAR", command=persistir)
        btn_finalizar.grid(column=1, pady=10, padx=10)
        btn_voltar = CTkButton(container, text="VOLTAR", command= top_pessoa_gravar.destroy)
        btn_voltar.grid(column=1, pady=10, padx=10)

    def apagar(self):
        def excluir():
            pessoa_id = texto_id.get()
            if self.controle.apagar(pessoa_id):
                ok_exc = CTkToplevel()
                ok_exc.title("")
                lbl_ok = CTkLabel(ok_exc, text="PESSOA EXCLUÍDA COM SUCESSO").grid(pady=10, padx=10)
                btn_ok = CTkButton(ok_exc, text="OK", command=lambda: [self.menu(2), ok_exc.destroy()]).grid(pady=10, padx=10)
                top_pessoa_exclusao.destroy()
            else:
                ok_exc = CTkToplevel()
                ok_exc.title("")
                lbl_ok = CTkLabel(ok_exc, text="Não há essa pessoa no banco.").grid(pady=10, padx=10)
                btn_ok = CTkButton(ok_exc, text="OK", command=ok_exc.destroy).grid(pady=10, padx=10)

        self.limpa_tela()
        top_pessoa_exclusao = CTkFrame(top_pessoa)
        top_pessoa_exclusao.grid(pady=10, padx=10)

        lbl_id_pessoa = CTkLabel(top_pessoa_exclusao, text="DIGITE O CPF DA PESSOA").grid(pady=10, padx=10)
        texto_id = CTkEntry(top_pessoa_exclusao, font=("Helvetica", 18))
        texto_id.grid(pady=10)

        btn_insere = CTkButton(top_pessoa_exclusao, text="EXCLUIR PESSOA", command=excluir).grid(pady=10, padx=10)
        btn_voltar = CTkButton(top_pessoa_exclusao, text="VOLTAR",
                               command=lambda: self.menu(2)).grid(pady=10, padx=10)

    def buscar(self, tipo_user):
        def procura():
            termo = texto_id.get()
            achados = self.controle.buscar(termo)
            janela_achados = CTkToplevel()
            janela_achados.title("RESULTADO DA PESQUISA")
            janela_achados.geometry("1000x600")

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

            resultado['columns'] = ('nome', 'data', 'salario', 'telefone', 'funcao')
            resultado.column("#0", width=0,  stretch=NO)
            resultado.column("nome",anchor=CENTER, width=80)
            resultado.column("data",anchor=CENTER,width=80)
            resultado.column("salario",anchor=CENTER,width=80)
            resultado.column("telefone",anchor=CENTER,width=80)
            resultado.column("funcao",anchor=CENTER,width=80)

            resultado.heading("#0",text="",anchor=CENTER)
            resultado.heading("nome",text="Nome",anchor=CENTER)
            resultado.heading("data",text="Data de nascimento",anchor=CENTER)
            resultado.heading("salario",text="Salário (R$)",anchor=CENTER)
            resultado.heading("telefone",text="Telefone",anchor=CENTER)
            resultado.heading("funcao",text="Função",anchor=CENTER)

            for (indice, pessoa) in enumerate(achados):
                resultado.insert(parent='',index='end',iid=indice,text='',
                                 values=(pessoa[0],pessoa[2], pessoa[3], pessoa[4], pessoa[5]))

            lbl_janela = CTkLabel(janela_achados, text="RESULTADO DA PESQUISA").pack(pady=10, padx=10)

            btn_ok = CTkButton(janela_achados, text="OK", command=janela_achados.destroy).pack(pady=10, padx=10)

        self.limpa_tela()
        top_pessoa_buscar = CTkFrame(top_pessoa)
        top_pessoa_buscar.grid(pady=10, padx=10)

        lbl_id_pessoa = CTkLabel(top_pessoa_buscar, text="DIGITE O NOME DA PESSOA").grid(pady=10, padx=10)
        texto_id = CTkEntry(top_pessoa_buscar, font=("Helvetica", 18))
        texto_id.grid(pady=10)

        btn_buscar = CTkButton(top_pessoa_buscar, text="BUSCAR", command=procura)
        btn_buscar.grid(pady=10, padx=10)
        btn_voltar = CTkButton(top_pessoa_buscar, text="VOLTAR", command=lambda: self.menu(tipo_user))
        btn_voltar.grid(pady=10, padx=10)
