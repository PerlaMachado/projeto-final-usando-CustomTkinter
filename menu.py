import customtkinter as ctk
from calculadora import CalculadoraFrame
from cambio import CambioFrame
from excel_precos import ExcelFrame
from email_auto import EmailFrame

import tema
from cores import obter_cores


class MenuApp(ctk.CTkToplevel):

    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode(
            tema.tema_atual
        )

        cores = obter_cores()

        self.cor_fundo = cores["fundo"]

        self.cor_sidebar = cores["sidebar"]

        self.cor_card = cores["card"]

        self.cor_texto = cores["texto"]

        self.cor_botao = cores["botao"]

        self.cor_hover = cores["hover"]

        # Janela
        self.title("Sistema de Automação")

        self.geometry("1000x600")

        self.resizable(False, False)

        self.configure(
            fg_color=self.cor_fundo
        )

        # Sidebar
        self.sidebar = ctk.CTkFrame(
            self,
            width=220,
            fg_color=self.cor_sidebar,
            corner_radius=0
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        # Logo
        self.logo = ctk.CTkLabel(
            self.sidebar,
            text="⚡ Automação",
            font=("Segoe UI", 24, "bold"),
            text_color=self.cor_texto
        )

        self.logo.pack(
            pady=(40, 50)
        )

        # Botões menu
        self.botao_calc = self.criar_botao(
            "🧮 Calculadora",
            self.abrir_calculadora
        )

        self.botao_email = self.criar_botao(
            "📧 E-mail",
            self.abrir_email
        )

        self.botao_cambio = self.criar_botao(
            "💵 Cotação",
            self.abrir_cambio
        )

        self.botao_excel = self.criar_botao(
            "📊 Excel",
            self.abrir_excel
        )

        # Área principal
        self.area_principal = ctk.CTkFrame(
            self,
            fg_color=self.cor_fundo
        )

        self.area_principal.pack(
            side="right",
            expand=True,
            fill="both"
        )

        self.tela_inicial()

    def criar_botao(self, texto, comando):

        botao = ctk.CTkButton(
            self.sidebar,
            text=texto,
            height=45,
            fg_color=self.cor_card,
            hover_color=self.cor_hover,
            text_color=self.cor_texto,
            command=comando
        )

        botao.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        return botao

    def limpar_area(self):

        for widget in self.area_principal.winfo_children():

            widget.destroy()

    def resetar_botoes(self):

        botoes = [
            self.botao_calc,
            self.botao_email,
            self.botao_cambio,
            self.botao_excel
        ]

        for botao in botoes:

            botao.configure(
                fg_color=self.cor_card
            )

    def tela_inicial(self):

        self.limpar_area()

        titulo = ctk.CTkLabel(
            self.area_principal,
            text="Bem-vindo ao Sistema 🚀",
            font=("Segoe UI", 30, "bold"),
            text_color=self.cor_texto
        )

        titulo.pack(
            pady=(220, 20)
        )

    def abrir_calculadora(self):

        self.limpar_area()

        self.resetar_botoes()

        self.botao_calc.configure(
            fg_color=self.cor_botao
        )

        frame = CalculadoraFrame(
            self.area_principal
        )

        frame.pack(
            expand=True,
            fill="both"
        )

    def abrir_email(self):

        self.limpar_area()

        self.resetar_botoes()

        self.botao_email.configure(
            fg_color=self.cor_botao
        )

        frame = EmailFrame(
            self.area_principal
        )

        frame.pack(
            expand=True,
            fill="both"
        )

    def abrir_cambio(self):

        self.limpar_area()

        self.resetar_botoes()

        self.botao_cambio.configure(
            fg_color=self.cor_botao
        )

        frame = CambioFrame(
            self.area_principal
        )

        frame.pack(
            expand=True,
            fill="both"
        )

    def abrir_excel(self):

        self.limpar_area()

        self.resetar_botoes()

        self.botao_excel.configure(
            fg_color=self.cor_botao
        )

        frame = ExcelFrame(
            self.area_principal
        )

        frame.pack(
            expand=True,
            fill="both"
        )