import customtkinter as ctk
from tkinter import messagebox
from cores import cores


class CalculadoraFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        # 🎨 CORES (PADRÃO CORRETO)
        c = cores()

        self.cor_card = c["card"]
        self.cor_texto = c["texto"]
        self.cor_botao = c["botao"]
        self.cor_hover = c["hover"]

        self.configure(
            fg_color=c["fundo"]
        )

        # Título
        self.label_titulo = ctk.CTkLabel(
            self,
            text="🧮 Calculadora",
            font=("Segoe UI", 30, "bold"),
            text_color=self.cor_texto
        )

        self.label_titulo.pack(pady=(40, 20))

        # Card
        self.frame_card = ctk.CTkFrame(
            self,
            width=320,
            height=420,
            fg_color=self.cor_card,
            corner_radius=20
        )

        self.frame_card.pack()
        self.frame_card.pack_propagate(False)

        # Número 1
        self.entry_num1 = ctk.CTkEntry(
            self.frame_card,
            placeholder_text="Digite o primeiro número",
            width=250,
            height=45
        )

        self.entry_num1.pack(pady=(40, 20))

        # Número 2
        self.entry_num2 = ctk.CTkEntry(
            self.frame_card,
            placeholder_text="Digite o segundo número",
            width=250,
            height=45
        )

        self.entry_num2.pack(pady=10)

        # Operações
        self.frame_operacoes = ctk.CTkFrame(
            self.frame_card,
            fg_color="transparent"
        )

        self.frame_operacoes.pack(pady=25)

        operacoes = [
            ("+", self.somar),
            ("-", self.subtrair),
            ("×", self.multiplicar),
            ("÷", self.dividir)
        ]

        for texto, comando in operacoes:

            botao = ctk.CTkButton(
                self.frame_operacoes,
                text=texto,
                width=60,
                height=40,
                fg_color=self.cor_botao,
                hover_color=self.cor_hover,
                command=comando
            )

            botao.pack(side="left", padx=6)

        # Resultado
        self.label_resultado = ctk.CTkLabel(
            self.frame_card,
            text="Resultado:",
            font=("Segoe UI", 18, "bold"),
            text_color=self.cor_texto
        )

        self.label_resultado.pack(pady=(30, 10))

        # Limpar
        self.botao_limpar = ctk.CTkButton(
            self.frame_card,
            text="Limpar",
            width=250,
            height=45,
            fg_color="#EF4444",
            hover_color="#DC2626",
            command=self.limpar
        )

        self.botao_limpar.pack(pady=20)

    def obter_numeros(self):

        try:
            num1 = float(self.entry_num1.get())
            num2 = float(self.entry_num2.get())
            return num1, num2

        except:
            messagebox.showerror("Erro", "Digite números válidos!")
            return None

    def atualizar_resultado(self, valor):
        self.label_resultado.configure(text=f"Resultado: {valor}")

    def somar(self):
        numeros = self.obter_numeros()
        if numeros:
            num1, num2 = numeros
            self.atualizar_resultado(num1 + num2)

    def subtrair(self):
        numeros = self.obter_numeros()
        if numeros:
            num1, num2 = numeros
            self.atualizar_resultado(num1 - num2)

    def multiplicar(self):
        numeros = self.obter_numeros()
        if numeros:
            num1, num2 = numeros
            self.atualizar_resultado(num1 * num2)

    def dividir(self):
        numeros = self.obter_numeros()
        if numeros:
            num1, num2 = numeros

            if num2 == 0:
                messagebox.showerror("Erro", "Não é possível dividir por zero!")
                return

            self.atualizar_resultado(round(num1 / num2, 2))

    def limpar(self):
        self.entry_num1.delete(0, "end")
        self.entry_num2.delete(0, "end")
        self.label_resultado.configure(text="Resultado:")