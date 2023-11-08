from tkinter.ttk import Treeview
from customtkinter import *
from customtkinter.windows.widgets import ctk_button, ctk_entry

from visao.visao import Visao
from controle.controle import Controle
from modelo.jogador import Jogador

class JogadorVisao(Visao):
    def __init__(self, controle: Controle):
        super().__init__(controle)

    def limpa_tela(self):
        for widget in top_jogador.winfo_children():
            widget.grid_remove()

    def menu_inicial_jogador(self):
        self.limpa_tela()
        container = CTkFrame(top_jogador)
        container.grid(pady=10, padx=10)

        btn_voltar  = CTkButton(container, text="VOLTAR", command=top_jogador.destroy)
        btn_voltar.grid(pady=10, padx=10)
        btn_buscar = CTkButton(container, text="BUSCAR JOGADOR", command=self.buscar)
        btn_buscar.grid(pady=10, padx=10)
        pass

    def expandir_menu_jogador(self):
        pass

    def menu(self, tipo_user: int):
        global top_jogador
        top_jogador = CTk()
        top_jogador.geometry("350x450")
        top_jogador.resizable(0, 0)
        top_jogador.columnconfigure(0, weight=1)
        top_jogador.rowconfigure(0, weight=1)

        top_jogador.title("MENU DE JOGADOR")
        container = CTkFrame(top_jogador)
        container.grid(row=0, column=0)
        jogador_buscar = CTkButton(container, text="BUSCAR JOGADOR", command=self.buscar).grid(pady=10, padx=10)
        if tipo_user != 1:
            jogador_gravar = CTkButton(container, text="INSERIR JOGADOR", command=self.gravar)
            jogador_gravar.grid(pady=10, padx=10)
            jogador_apagar = CTkButton(container, text="EXCLUIR JOGADOR", command=self.apagar)
            jogador_apagar.grid(pady=10, padx=10)
        jogador_voltar = CTkButton(container, text="VOLTAR AO MENU INICIAL", command=top_jogador.destroy).grid(pady=10, padx=10)

    def gravar(self):
        def persistir():
            nome = texto_nome.get()
            cpf = texto_cpf.get()
            data = f"{texto_ano.get()}-{texto_mes.get()}-{texto_dia.get()}"
            salario = float( texto_salario.get() )
            telefone = texto_telefone.get()
            numero_camisa = int( texto_camisa.get() )
            funcao = texto_funcao.get()
            posicao = texto_posicao.get()
            global o_jogador
            o_jogador = Jogador(nome, cpf, data, salario, telefone, numero_camisa, funcao, posicao)

        top_jogador_gravar = CTk()
        top_jogador_gravar.geometry("800x800")
        top_jogador_gravar.columnconfigure(0, weight=1)
        top_jogador_gravar.rowconfigure(0, weight=1)
        top_jogador_gravar.title("INSERIR JOGADOR")
        container = CTkFrame(top_jogador_gravar)
        container.grid(pady=10, padx=10)

        label_nome_jogador = CTkLabel(container, text="DIGITE O NOME DO JOGADOR")
        label_nome_jogador.grid(row=0, column=1)
        texto_nome = CTkEntry(container, font=("Helvetica", 18))
        texto_nome.grid(column=1, row=1, pady=10, padx=10)

        label_cpf_jogador = CTkLabel(container, text="DIGITE O CPF DO JOGADOR")
        label_cpf_jogador.grid(row=2, column=1)
        texto_cpf = CTkEntry(container, font=("Helvetica", 18))
        texto_cpf.grid(column=1, row=3,pady=10, padx=10)

        label_data_jogador = CTkLabel(container, text="DIGITE A DATA DE\nNASCIMENTO DO JOGADOR")
        label_data_jogador.grid(row=4, column=1)
        texto_dia = CTkEntry(container)
        texto_dia.grid(column=0, row=5, pady=10, padx=10)
        texto_mes = CTkEntry(container)
        texto_mes.grid(column=1, row=5, pady=10, padx=10)
        texto_ano = CTkEntry(container)
        texto_ano.grid(column=2, row=5, pady=10, padx=10)

        label_salario_jogador = CTkLabel(container, text="DIGITE O SALARIO DO JOGADOR")
        label_salario_jogador.grid(row=6, column=1)
        texto_salario = CTkEntry(container)
        texto_salario.grid(column=1,row=7,pady=10, padx=10)
    
        label_telefone_jogador = CTkLabel(container, text="DIGITE O TELEFONE DO JOGADOR")
        label_telefone_jogador.grid(row=8, column=1)
        texto_telefone = CTkEntry(container)
        texto_telefone.grid(column=1,row=9,pady=10)

        label_camisa_jogador = CTkLabel(container, text="DIGITE O NÚMERO\nDA CAMISA DO JOGADOR")
        label_camisa_jogador.grid(row=10, column=1)
        texto_camisa = CTkEntry(container)
        texto_camisa.grid(column=1,row=11,pady=10)

        label_funcao_jogador = CTkLabel(container, text="DIGITE A FUNÇÃO DO JOGADOR")
        label_funcao_jogador.grid(row=12, column=1)
        texto_funcao = CTkEntry(container)
        texto_funcao.grid(column=1,row=13,pady=10)

        label_posicao_jogador = CTkLabel(container, text="DIGITE A POSIÇÃO DO JOGADOR")
        label_posicao_jogador.grid(row=14, column=1)
        texto_posicao = CTkEntry(container)
        texto_posicao.grid(column=1,row=15,pady=10)


        btn_finalizar = CTkButton(container, text="FINALIZAR", command=persistir)
        btn_finalizar.grid(column=1, pady=10, padx=10)
        btn_voltar = CTkButton(container, text="VOLTAR", command= top_jogador_gravar.destroy)
        btn_voltar.grid(column=1, pady=10, padx=10)

    def apagar(self):
        def excluir():
            jogador_id = int(texto_id.get())
            if self.controle.buscaID(jogador_id) != -1:
                self.controle.exclusao(self.controle.buscaID(jogador_id))
                ok_exc = CTkToplevel()
                ok_exc.title("")
                lbl_ok = CTkLabel(ok_exc, text="JOGADOR EXCLUÍDO COM SUCESSO").grid(pady=10, padx=10)
                btn_ok = CTkButton(ok_exc, text="OK", command=ok_exc.destroy).grid(pady=10, padx=10)
                top_jogador_exclusao.destroy()
            else:
                ok_exc = CTkToplevel()
                ok_exc.title("")
                lbl_ok = CTkLabel(ok_exc, text="Não há esse jogador no banco.").grid(pady=10, padx=10)
                btn_ok = CTkButton(ok_exc, text="OK", command=ok_exc.destroy).grid(pady=10, padx=10)

        top_jogador_exclusao = CTkToplevel()
        top_jogador_exclusao.title("EXCLUIR JOGADOR")

        lbl_id_jogador = CTkLabel(top_jogador_exclusao, text="DIGITE O ID DA JOGADOR").grid(pady=10, padx=10)
        texto_id = CTkEntry(top_jogador_exclusao, font=("Helvetica", 18))
        texto_id.grid(pady=10)

        btn_insere = CTkButton(top_jogador_exclusao, text="EXCLUIR JOGADOR", command=excluir).grid(pady=10, padx=10)
        btn_voltar = CTkButton(top_jogador_exclusao, text="VOLTAR",
                            command=top_jogador_exclusao.destroy).grid(pady=10, padx=10)

    def buscar(self):
        def procura():
            termo = texto_id.get()
            achados = self.controle.buscar(termo)
            janela_achados = CTkToplevel()
            janela_achados.title("RESULTADO DA PESQUISA")
            janela_achados.geometry("500x500")

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

            resultado['columns'] = ('nome', 'cpf', 'data', 'salario', 'telefone', 'funcao')
            resultado.column("#0", width=0,  stretch=NO)
            resultado.column("nome",anchor=CENTER, width=80)
            resultado.column("cpf",anchor=CENTER,width=80)
            resultado.column("data",anchor=CENTER,width=80)
            resultado.column("salario",anchor=CENTER,width=80)
            resultado.column("telefone",anchor=CENTER,width=80)
            resultado.column("funcao",anchor=CENTER,width=80)

            resultado.heading("#0",text="",anchor=CENTER)
            resultado.heading("nome",text="Nome",anchor=CENTER)
            resultado.heading("cpf",text="CPF",anchor=CENTER)
            resultado.heading("data",text="Data de nascimento",anchor=CENTER)
            resultado.heading("salario",text="Salário (R$)",anchor=CENTER)
            resultado.heading("telefone",text="Telefone",anchor=CENTER)
            resultado.heading("funcao",text="Função",anchor=CENTER)

            for (indice, jogador) in enumerate(achados):
                resultado.insert(parent='',index='end',iid=indice,text='',
                                 values=(jogador[0],jogador[1], jogador[2], jogador[3], jogador[4], jogador[5]))


            lbl_janela = CTkLabel(janela_achados, text="RESULTADO DA PESQUISA").pack(pady=10, padx=10)

            btn_ok = CTkButton(janela_achados, text="OK", command=janela_achados.destroy).pack(pady=10, padx=10)

        self.limpa_tela()
        top_jogador_buscar = CTkFrame(top_jogador)
        top_jogador_buscar.grid(pady=10, padx=10)

        lbl_id_jogador = CTkLabel(top_jogador_buscar, text="DIGITE O NOME DO JOGADOR").grid(pady=10, padx=10)
        texto_id = CTkEntry(top_jogador_buscar, font=("Helvetica", 18))
        texto_id.grid(pady=10)

        btn_buscar = CTkButton(top_jogador_buscar, text="BUSCAR", command=procura)
        btn_buscar.grid(pady=10, padx=10)
        btn_voltar = CTkButton(top_jogador_buscar, text="VOLTAR", command=self.menu_inicial_jogador)
        btn_voltar.grid(pady=10, padx=10)
