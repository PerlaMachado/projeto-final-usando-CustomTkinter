import customtkinter as ctk
from tkinter import ttk, messagebox
import pandas as pd
import json
import os
from cores import cores


class ExcelFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        # =========================
        # CORES GLOBAIS
        # =========================
        c = cores()

        self.cor_card = c["card"]
        self.cor_texto = c["texto"]
        self.cor_botao = c["botao"]
        self.cor_hover = c["hover"]

        self.configure(fg_color="transparent")

        # =========================
        # ARQUIVOS
        # =========================
        self.pasta_arquivos = "arquivos"
        os.makedirs(self.pasta_arquivos, exist_ok=True)

        self.arquivo_json = "arquivos/produtos.json"
        self.arquivo_excel = "arquivos/controle_precos.xlsx"

        # =========================
        # DADOS
        # =========================
        self.produtos = []
        self.carregar_produtos()

        # =========================
        # TÍTULO
        # =========================
        self.label_titulo = ctk.CTkLabel(
            self,
            text="📊 Controle de Preços",
            font=("Segoe UI", 28, "bold"),
            text_color=self.cor_texto
        )

        self.label_titulo.pack(pady=(20, 20))

        # =========================
        # CARD PRINCIPAL
        # =========================
        self.frame_card = ctk.CTkFrame(
            self,
            width=750,
            height=500,
            fg_color=self.cor_card,
            corner_radius=20
        )

        self.frame_card.pack(pady=10)
        self.frame_card.pack_propagate(False)

        # =========================
        # INPUTS
        # =========================
        self.frame_inputs = ctk.CTkFrame(
            self.frame_card,
            fg_color="transparent"
        )

        self.frame_inputs.pack(pady=(25, 15))

        self.entry_produto = ctk.CTkEntry(
            self.frame_inputs,
            placeholder_text="Nome do produto",
            width=250,
            height=40
        )

        self.entry_produto.grid(row=0, column=0, padx=10)

        self.entry_preco = ctk.CTkEntry(
            self.frame_inputs,
            placeholder_text="Preço atual",
            width=180,
            height=40
        )

        self.entry_preco.grid(row=0, column=1, padx=10)

        # =========================
        # BOTÕES
        # =========================
        self.frame_botoes = ctk.CTkFrame(
            self.frame_card,
            fg_color="transparent"
        )

        self.frame_botoes.pack(pady=10)

        self.botao_adicionar = ctk.CTkButton(
            self.frame_botoes,
            text="Adicionar Produto",
            width=180,
            height=40,
            fg_color=self.cor_botao,
            hover_color=self.cor_hover,
            command=self.adicionar_produto
        )

        self.botao_adicionar.grid(row=0, column=0, padx=10)

        self.botao_atualizar = ctk.CTkButton(
            self.frame_botoes,
            text="Atualizar Preço",
            width=180,
            height=40,
            fg_color="#F59E0B",
            hover_color="#D97706",
            command=self.atualizar_preco
        )

        self.botao_atualizar.grid(row=0, column=1, padx=10)

        self.botao_remover = ctk.CTkButton(
            self.frame_botoes,
            text="Remover",
            width=140,
            height=40,
            fg_color="#EF4444",
            hover_color="#DC2626",
            command=self.remover_produto
        )

        self.botao_remover.grid(row=0, column=2, padx=10)

        # =========================
        # FRAME TABELA (ESTÁVEL)
        # =========================
        self.frame_tabela = ctk.CTkFrame(
            self.frame_card,
            fg_color="#F3F4F6"  # neutro fixo para evitar invisibilidade
        )

        self.frame_tabela.pack(
            padx=20,
            pady=20,
            fill="both",
            expand=True
        )

        # =========================
        # ESTILO DO TREEVIEW (ESTÁVEL)
        # =========================
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Treeview",
            background="#F9FAFB",
            foreground="#111111",
            fieldbackground="#F9FAFB",
            rowheight=28
        )

        style.configure(
            "Treeview.Heading",
            background="#E5E7EB",
            foreground="#111111",
            font=("Segoe UI", 10, "bold")
        )

        style.map(
            "Treeview",
            background=[("selected", "#3B82F6")],
            foreground=[("selected", "white")]
        )

        # =========================
        # TABELA
        # =========================
        self.tabela = ttk.Treeview(
            self.frame_tabela,
            columns=("Produto", "Antigo", "Atual", "Status"),
            show="headings"
        )

        self.tabela.heading("Produto", text="Produto")
        self.tabela.heading("Antigo", text="Preço Antigo")
        self.tabela.heading("Atual", text="Preço Atual")
        self.tabela.heading("Status", text="Status")

        self.tabela.column("Produto", width=220)
        self.tabela.column("Antigo", width=140)
        self.tabela.column("Atual", width=140)
        self.tabela.column("Status", width=120)

        self.tabela.pack(fill="both", expand=True)

        # =========================
        # EXPORTAR
        # =========================
        self.botao_exportar = ctk.CTkButton(
            self.frame_card,
            text="Exportar Excel",
            width=240,
            height=45,
            fg_color="#22C55E",
            hover_color="#16A34A",
            command=self.exportar_excel
        )

        self.botao_exportar.pack(pady=(0, 20))

        # FORÇA CARREGAMENTO
        self.after(100, self.atualizar_tabela)

    # =========================
    # JSON
    # =========================
    def salvar_produtos(self):
        with open(self.arquivo_json, "w", encoding="utf-8") as f:
            json.dump(self.produtos, f, indent=4, ensure_ascii=False)

    def carregar_produtos(self):
        if os.path.exists(self.arquivo_json):
            with open(self.arquivo_json, "r", encoding="utf-8") as f:
                self.produtos = json.load(f)

    # =========================
    # ADICIONAR
    # =========================
    def adicionar_produto(self):

        produto = self.entry_produto.get()
        preco = self.entry_preco.get()

        if not produto or not preco:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

        try:
            preco = float(preco)
        except:
            messagebox.showerror("Erro", "Preço inválido!")
            return

        self.produtos.append({
            "produto": produto,
            "antigo": "--",
            "atual": preco,
            "status": "Novo"
        })

        self.salvar_produtos()
        self.atualizar_tabela()
        self.limpar_campos()

    # =========================
    # ATUALIZAR
    # =========================
    def atualizar_preco(self):

        item = self.tabela.selection()
        if not item:
            messagebox.showwarning("Aviso", "Selecione um produto!")
            return

        try:
            novo_preco = float(self.entry_preco.get())
        except:
            messagebox.showerror("Erro", "Preço inválido!")
            return

        indice = self.tabela.index(item)
        produto = self.produtos[indice]

        antigo = produto["atual"]
        produto["antigo"] = antigo
        produto["atual"] = novo_preco

        if novo_preco > antigo:
            produto["status"] = "▲ Aumentou"
        elif novo_preco < antigo:
            produto["status"] = "▼ Diminuiu"
        else:
            produto["status"] = "▬ Igual"

        self.salvar_produtos()
        self.atualizar_tabela()
        self.limpar_campos()

    # =========================
    # REMOVER
    # =========================
    def remover_produto(self):

        item = self.tabela.selection()

        if not item:
            messagebox.showwarning("Aviso", "Selecione um produto!")
            return

        indice = self.tabela.index(item)

        del self.produtos[indice]

        self.salvar_produtos()
        self.atualizar_tabela()

    # =========================
    # TABELA
    # =========================
    def atualizar_tabela(self):

        for i in self.tabela.get_children():
            self.tabela.delete(i)

        for p in self.produtos:

            antigo = p["antigo"]
            if antigo != "--":
                antigo = f"R$ {antigo:.2f}"

            atual = f"R$ {p['atual']:.2f}"

            self.tabela.insert(
                "",
                "end",
                values=(p["produto"], antigo, atual, p["status"])
            )

    # =========================
    # EXPORTAR
    # =========================
    def exportar_excel(self):

        if not self.produtos:
            messagebox.showwarning("Aviso", "Sem produtos!")
            return

        df = pd.DataFrame(self.produtos)
        df.to_excel(self.arquivo_excel, index=False)

        messagebox.showinfo("Sucesso", "Excel exportado!")

    # =========================
    # LIMPAR
    # =========================
    def limpar_campos(self):
        self.entry_produto.delete(0, "end")
        self.entry_preco.delete(0, "end")