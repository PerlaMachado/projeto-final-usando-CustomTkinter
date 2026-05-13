import customtkinter as ctk
from tkinter import messagebox
from cores import cores


class CalculadoraFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        c = cores()

        self.cor_fundo = c["fundo"]
        self.cor_card = c["card"]
        self.cor_texto = c["texto"]
        self.cor_botao = c["botao"]
        self.cor_hover = c["hover"]

        self.configure(
            fg_color=self.cor_fundo
        )

        self.expressao = ""

        self.label_titulo = ctk.CTkLabel(
            self,
            text="🧮 Central de Cálculos",
            font=("Segoe UI", 24, "bold"),
            text_color=self.cor_texto
        )

        self.label_titulo.pack(
            pady=(15, 5)
        )

        self.frame_principal = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.frame_principal.pack(
            expand=True,
            fill="both",
            padx=20,
            pady=10
        )

        self.frame_card = ctk.CTkFrame(
            self.frame_principal,
            width=390,
            height=500,
            fg_color=self.cor_card,
            corner_radius=20
        )

        self.frame_card.pack(
            side="left",
            padx=(20, 10),
            pady=10
        )

        self.frame_card.pack_propagate(False)

        self.frame_visor = ctk.CTkFrame(
            self.frame_card,
            width=320,
            height=80,
            fg_color="#111827",
            corner_radius=12
        )

        self.frame_visor.pack(
            pady=(20, 15)
        )

        self.frame_visor.pack_propagate(False)

        self.label_visor = ctk.CTkLabel(
            self.frame_visor,
            text="0",
            font=("Segoe UI", 28, "bold"),
            text_color="white"
        )

        self.label_visor.place(
            relx=0.95,
            rely=0.5,
            anchor="e"
        )

        self.frame_teclado = ctk.CTkFrame(
            self.frame_card,
            fg_color="transparent"
        )

        self.frame_teclado.pack(
            pady=(5, 0)
        )

        botoes = [

            ("7", "#374151"),
            ("8", "#374151"),
            ("9", "#374151"),
            ("÷", self.cor_botao),

            ("4", "#374151"),
            ("5", "#374151"),
            ("6", "#374151"),
            ("×", self.cor_botao),

            ("1", "#374151"),
            ("2", "#374151"),
            ("3", "#374151"),
            ("-", self.cor_botao),

            ("0", "#374151"),
            (".", "#374151"),
            ("C", "#EF4444"),
            ("+", self.cor_botao),

            ("√", "#8B5CF6"),
            ("x²", "#8B5CF6"),
            ("%", "#F59E0B"),
            ("=", "#22C55E")

        ]

        linha = 0
        coluna = 0

        for texto, cor in botoes:

            botao = ctk.CTkButton(
                self.frame_teclado,
                text=texto,
                width=68,
                height=50,
                corner_radius=12,
                fg_color=cor,
                hover_color=self.cor_hover,
                font=("Segoe UI", 18, "bold"),
                command=lambda t=texto: self.clique(t)
            )

            botao.grid(
                row=linha,
                column=coluna,
                padx=5,
                pady=5
            )

            coluna += 1

            if coluna > 3:

                coluna = 0
                linha += 1

        self.label_resultado = ctk.CTkLabel(
            self.frame_card,
            text="Pronto para calcular",
            font=("Segoe UI", 14),
            text_color="#9CA3AF"
        )

        self.label_resultado.pack(
            pady=(15, 0)
        )

        self.frame_historico = ctk.CTkFrame(
            self.frame_principal,
            width=240,
            height=500,
            fg_color=self.cor_card,
            corner_radius=20
        )

        self.frame_historico.pack(
            side="left",
            padx=(10, 20),
            pady=10
        )

        self.frame_historico.pack_propagate(False)

        self.label_historico = ctk.CTkLabel(
            self.frame_historico,
            text="📜 Histórico",
            font=("Segoe UI", 20, "bold"),
            text_color=self.cor_texto
        )

        self.label_historico.pack(
            pady=(20, 10)
        )

        self.textbox_historico = ctk.CTkTextbox(
            self.frame_historico,
            width=200,
            height=380,
            corner_radius=12,
            font=("Consolas", 13),
            fg_color="#111827",
            text_color="white"
        )

        self.textbox_historico.pack(
            pady=10
        )

        self.janela = self.winfo_toplevel()

        self.janela.bind(
            "<Key>",
            self.teclado_fisico
        )

    def clique(self, valor):

        if valor == "=":

            self.calcular()
            return

        if valor == "C":

            self.limpar()
            return

        if valor == "×":
            valor = "*"

        if valor == "÷":
            valor = "/"

        if valor == "√":

            try:

                resultado = eval(self.expressao) ** 0.5

                resultado = round(resultado, 2)

                self.adicionar_historico(
                    f"√({self.expressao}) = {resultado}"
                )

                self.expressao = str(resultado)

                self.label_visor.configure(
                    text=self.expressao
                )

            except:

                messagebox.showerror(
                    "Erro",
                    "Cálculo inválido!"
                )

            return

        if valor == "x²":

            try:

                resultado = eval(self.expressao) ** 2

                self.adicionar_historico(
                    f"({self.expressao})² = {resultado}"
                )

                self.expressao = str(resultado)

                self.label_visor.configure(
                    text=self.expressao
                )

            except:

                messagebox.showerror(
                    "Erro",
                    "Cálculo inválido!"
                )

            return

        self.expressao += valor

        self.label_visor.configure(
            text=self.expressao
        )

    def teclado_fisico(self, event):

        tecla = event.char

        permitidos = "0123456789+-*/.%"

        if tecla in permitidos:

            self.expressao += tecla

            self.label_visor.configure(
                text=self.expressao
            )

        elif event.keysym == "Return":

            self.calcular()

        elif event.keysym == "BackSpace":

            self.expressao = self.expressao[:-1]

            if self.expressao == "":

                self.label_visor.configure(
                    text="0"
                )

            else:

                self.label_visor.configure(
                    text=self.expressao
                )

        elif event.keysym == "Escape":

            self.limpar()

    def calcular(self):

        try:

            resultado = eval(self.expressao)

            self.label_resultado.configure(
                text=f"Resultado: {resultado}"
            )

            self.adicionar_historico(
                f"{self.expressao} = {resultado}"
            )

            self.expressao = str(resultado)

            self.label_visor.configure(
                text=self.expressao
            )

        except:

            messagebox.showerror(
                "Erro",
                "Expressão inválida!"
            )

    def adicionar_historico(self, texto):

        self.textbox_historico.insert(
            "end",
            texto + "\n"
        )

        self.textbox_historico.see("end")

    def limpar(self):

        self.expressao = ""

        self.label_visor.configure(
            text="0"
        )

        self.label_resultado.configure(
            text="Pronto para calcular"
        )