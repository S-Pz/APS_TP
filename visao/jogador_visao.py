from tkinter import Label, Toplevel
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
        container.grid()

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
        #top_jogador.destroy()

        top_jogador_gravar = CTk()
        top_jogador_gravar.geometry("800x800")
        top_jogador_gravar.columnconfigure(0, weight=1)
        top_jogador_gravar.rowconfigure(0, weight=1)
        top_jogador_gravar.title("INSERIR JOGADOR")
        container = CTkFrame(top_jogador_gravar)
        container.grid()

        label_nome_jogador = CTkLabel(container, text="DIGITE O NOME DO JOGADOR")
        label_nome_jogador.grid(row=0, column=1)
        texto_nome = CTkEntry(container, font=("Helvetica", 18))
        texto_nome.grid(column=1, row=1, pady=10, padx=10)
        nome = texto_nome.get()

        label_cpf_jogador = CTkLabel(container, text="DIGITE O CPF DO JOGADOR")
        label_cpf_jogador.grid(row=2, column=1)
        texto_cpf = CTkEntry(container, font=("Helvetica", 18))
        texto_cpf.grid(column=1, row=3,pady=10, padx=10)
        cpf = texto_cpf.get()

        label_data_jogador = CTkLabel(container, text="DIGITE A DATA DE\nNASCIMENTO DO JOGADOR")
        label_data_jogador.grid(row=4, column=1)
        texto_dia = CTkEntry(container)
        texto_dia.grid(column=0, row=5, pady=10, padx=10)
        texto_mes = CTkEntry(container)
        texto_mes.grid(column=1, row=5, pady=10, padx=10)
        texto_ano = CTkEntry(container)
        texto_ano.grid(column=2, row=5, pady=10, padx=10)
        data = f"{texto_ano.get()}-{texto_mes.get()}-{texto_dia.get()}"

        label_salario_jogador = CTkLabel(container, text="DIGITE O SALARIO DO JOGADOR")
        label_salario_jogador.grid(row=6, column=1)
        texto_salario = CTkEntry(container)
        texto_salario.grid(column=1,row=7,pady=10, padx=10)
        salario = texto_salario.get()
    
        label_telefone_jogador = CTkLabel(container, text="DIGITE O TELEFONE DO JOGADOR")
        label_telefone_jogador.grid(row=8, column=1)
        texto_telefone = CTkEntry(container)
        texto_telefone.grid(column=1,row=9,pady=10)
        telefone = texto_telefone.get()

        label_camisa_jogador = CTkLabel(container, text="DIGITE O NÚMERO\nDA CAMISA DO JOGADOR")
        label_camisa_jogador.grid(row=10, column=1)
        texto_camisa = CTkEntry(container)
        texto_camisa.grid(column=1,row=11,pady=10)
        numero_camisa = texto_camisa.get()

        label_funcao_jogador = CTkLabel(container, text="DIGITE A FUNÇÃO DO JOGADOR")
        label_funcao_jogador.grid(row=12, column=1)
        texto_funcao = CTkEntry(container)
        texto_funcao.grid(column=1,row=13,pady=10)
        funcao = texto_funcao.get()

        label_posicao_jogador = CTkLabel(container, text="DIGITE A POSIÇÃO DO JOGADOR")
        label_posicao_jogador.grid(row=14, column=1)
        texto_posicao = CTkEntry(container)
        texto_posicao.grid(column=1,row=15,pady=10)
        posicao = texto_posicao.get()

        global o_jogador
        o_jogador = Jogador(nome, cpf, data, salario, telefone, numero_camisa, funcao, posicao)

        btn_finalizar = CTkButton(container, text="FINALIZAR", command= lambda: self.controle.gravar(o_jogador))
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
                lbl_ok = CTkLabel(ok_exc, text="JOGADOR EXCLUÍDA COM SUCESSO").grid()
                btn_ok = CTkButton(ok_exc, text="OK", command=ok_exc.destroy).grid()
                top_jogador_exclusao.destroy()
            else:
                ok_exc = CTkToplevel()
                ok_exc.title("")
                lbl_ok = CTkLabel(ok_exc, text="Não há uma jogador com esse ID.").grid()
                btn_ok = CTkButton(ok_exc, text="OK", command=ok_exc.destroy).grid()

        top_jogador_exclusao = CTkToplevel()
        top_jogador_exclusao.title("EXCLUIR JOGADOR")

        lbl_id_jogador = CTkLabel(top_jogador_exclusao, text="DIGITE O ID DA JOGADOR").grid()
        texto_id = CTkEntry(top_jogador_exclusao, font=("Helvetica", 18))
        texto_id.grid(pady=10)

        btn_insere = CTkButton(top_jogador_exclusao, text="EXCLUIR JOGADOR", command=excluir).grid()
        btn_voltar = CTkButton(top_jogador_exclusao, text="VOLTAR",
                            command=top_jogador_exclusao.destroy).grid()

    def buscar(self):
        self.limpa_tela()
        top_jogador_buscar = CTkFrame(top_jogador)
        top_jogador_buscar.grid()

        lbl_id_jogador = CTkLabel(top_jogador_buscar, text="DIGITE O NOME DO JOGADOR").grid()
        texto_id = CTkEntry(top_jogador_buscar, font=("Helvetica", 18))
        texto_id.grid(pady=10)

        btn_buscar = CTkButton(top_jogador_buscar, text="BUSCAR", command=self.controle.buscar(self.o_jogador))
        btn_buscar.grid(pady=10, padx=10)
        btn_voltar = CTkButton(top_jogador_buscar, text="VOLTAR", command=self.menu_inicial_jogador)
        btn_voltar.grid(pady=10, padx=10)
