import tkinter as tk
from tkinter import ttk
import crud as crud

class PrincipalBD:
    def __init__(self, win):
        self.objBD = crud.AppBD()

        # Componentes
        self.lblCodigo = tk.Label(win, text='Código do Produto:')
        self.lblNome = tk.Label(win, text='Nome do Produto')
        self.lblPreco = tk.Label(win, text='Preço')

        self.txtCodigo = tk.Entry(win, bd=3)
        self.txtNome = tk.Entry(win, bd=3)
        self.txtPreco = tk.Entry(win, bd=3)

        self.btnCadastrar = tk.Button(win, text='Cadastrar', command=self.fCadastrarProduto)
        self.btnAtualizar = tk.Button(win, text='Atualizar', command=self.fAtualizarProduto)
        self.btnExcluir = tk.Button(win, text='Excluir', command=self.fExcluirProduto)
        self.btnLimpar = tk.Button(win, text='Limpar', command=self.fLimparTela)

        # Componente TreeView
        self.dadosColunas = ("Código", "Nome", "Preço")

        self.treeProdutos = ttk.Treeview(win,
                                         columns=self.dadosColunas,
                                         selectmode='browse')

        self.verscrlbar = ttk.Scrollbar(win,
                                        orient="vertical",
                                        command=self.treeProdutos.yview)

        self.verscrlbar.pack(side='right', fill='y')

        self.treeProdutos.configure(yscrollcommand=self.verscrlbar.set)

        self.treeProdutos.heading("Código", text="Código")
        self.treeProdutos.heading("Nome", text="Nome")
        self.treeProdutos.heading("Preço", text="Preço")

        self.treeProdutos.column("Código", minwidth=0, width=100)
        self.treeProdutos.column("Nome", minwidth=0, width=100)
        self.treeProdutos.column("Preço", minwidth=0, width=100)

        self.treeProdutos.pack(padx=10, pady=10)

        self.treeProdutos.bind("<<TreeviewSelect>>", self.apresentarRegistrosSelecionados)

        # Posicionamento dos componentes na janela
        self.lblCodigo.place(x=100, y=50)
        self.txtCodigo.place(x=250, y=50)

        self.lblNome.place(x=100, y=100)
        self.txtNome.place(x=250, y=100)

        self.lblPreco.place(x=100, y=150)
        self.txtPreco.place(x=250, y=150)

        self.btnCadastrar.place(x=100, y=200)
        self.btnAtualizar.place(x=200, y=200)
        self.btnExcluir.place(x=300, y=200)
        self.btnLimpar.place(x=400, y=200)

        self.treeProdutos.place(x=100, y=300)
        self.verscrlbar.place(x=805, y=300, height=225)

        self.carregarDadosIniciais()

    def apresentarRegistrosSelecionados(self, event):
        self.fLimparTela()
        for selection in self.treeProdutos.selection():
            item = self.treeProdutos.item(selection)
            codigo, nome, preco = item["values"][0:3]
            self.txtCodigo.insert(0, codigo)
            self.txtNome.insert(0, nome)
            self.txtPreco.insert(0, preco)

    def carregarDadosIniciais(self):
        try:
            registros = self.objBD.selecionarDados()
            for item in registros:
                codigo, nome, preco = item
                self.treeProdutos.insert('', 'end', values=(codigo, nome, preco))
        except Exception as e:
            print("Erro ao carregar dados:", e)

    def fLerCampos(self):
        try:
            codigo = int(self.txtCodigo.get())
            nome = self.txtNome.get()
            preco = float(self.txtPreco.get())
            return codigo, nome, preco
        except ValueError as e:
            print('Erro na leitura dos campos:', e)

    def fCadastrarProduto(self):
        try:
            codigo, nome, preco = self.fLerCampos()
            self.objBD.inserirDados(codigo, nome, preco)
            self.treeProdutos.insert('', 'end', values=(codigo, nome, preco))
            self.fLimparTela()
        except Exception as e:
            print('Erro ao cadastrar produto:', e)

    def fAtualizarProduto(self):
        try:
            codigo, nome, preco = self.fLerCampos()
            self.objBD.atualizarDados(codigo, nome, preco)
            self.treeProdutos.delete(*self.treeProdutos.get_children())
            self.carregarDadosIniciais()
            self.fLimparTela()
        except Exception as e:
            print('Erro ao atualizar produto:', e)

    def fExcluirProduto(self):
        try:
            codigo, _, _ = self.fLerCampos()
            self.objBD.excluirDados(codigo)
            self.treeProdutos.delete(*self.treeProdutos.get_children())
            self.carregarDadosIniciais()
            self.fLimparTela()
        except Exception as e:
            print('Erro ao excluir produto:', e)

    def fLimparTela(self):
        self.txtCodigo.delete(0, tk.END)
        self.txtNome.delete(0, tk.END)
        self.txtPreco.delete(0, tk.END)

# Programa Principal
janela = tk.Tk()
principal = PrincipalBD(janela)
janela.title('Bem Vindo a Aplicação de Banco de Dados')
janela.geometry("820x600+10+10")
janela.mainloop()
