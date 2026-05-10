import customtkinter as ctk
import requests
from tkinter import messagebox
from datetime import datetime


class CambioFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        # =========================
        # CORES
        # =========================
        self.cor_card = "#2A2D3E"

        self.cor_botao = "#3B82F6"
        self.cor_hover = "#2563EB"

        self.configure(
            fg_color="transparent"
        )

        # =========================
        # TÍTULO
        # =========================
        self.label_titulo = ctk.CTkLabel(
            self,
            text="💵 Cotação de Moedas",
            font=("Segoe UI", 28, "bold"),
            text_color="white"
        )

        self.label_titulo.pack(
            pady=(30, 20)
        )

        # =========================
        # CARD PRINCIPAL
        # =========================
        self.frame_card = ctk.CTkFrame(
            self,
            width=500,
            height=350,
            fg_color=self.cor_card,
            corner_radius=20
        )

        self.frame_card.pack(
            pady=10
        )

        self.frame_card.pack_propagate(False)

        # =========================
        # TEXTO INFORMATIVO
        # =========================
        self.label_info = ctk.CTkLabel(
            self.frame_card,
            text="Consultar cotações em tempo real",
            font=("Segoe UI", 16),
            text_color="#B0B3C0"
        )

        self.label_info.pack(
            pady=(35, 20)
        )

        # =========================
        # DÓLAR
        # =========================
        self.label_dolar = ctk.CTkLabel(
            self.frame_card,
            text="Dólar: --",
            font=("Segoe UI", 24, "bold"),
            text_color="white"
        )

        self.label_dolar.pack(
            pady=15
        )

        # =========================
        # EURO
        # =========================
        self.label_euro = ctk.CTkLabel(
            self.frame_card,
            text="Euro: --",
            font=("Segoe UI", 24, "bold"),
            text_color="white"
        )

        self.label_euro.pack(
            pady=15
        )

        # =========================
        # HORÁRIO
        # =========================
        self.label_horario = ctk.CTkLabel(
            self.frame_card,
            text="Consulta não realizada",
            font=("Segoe UI", 15),
            text_color="#B0B3C0"
        )

        self.label_horario.pack(
            pady=20
        )

        # =========================
        # BOTÃO CONSULTAR
        # =========================
        self.botao_consultar = ctk.CTkButton(
            self.frame_card,
            text="Atualizar Cotação",
            width=220,
            height=45,
            corner_radius=12,
            fg_color=self.cor_botao,
            hover_color=self.cor_hover,
            font=("Segoe UI", 15, "bold"),
            command=self.buscar_cotacoes
        )

        self.botao_consultar.pack(
            pady=20
        )

    # ===================================
    # BUSCAR COTAÇÕES
    # ===================================
    def buscar_cotacoes(self):

        try:

            url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL"

            resposta = requests.get(
                url,
                timeout=5
            )

            dados = resposta.json()

            dolar = dados["USDBRL"]["bid"]

            euro = dados["EURBRL"]["bid"]

            # Atualiza dólar
            self.label_dolar.configure(
                text=f"Dólar: R$ {float(dolar):.2f}"
            )

            # Atualiza euro
            self.label_euro.configure(
                text=f"Euro: R$ {float(euro):.2f}"
            )

            # Hora atual
            horario = datetime.now().strftime(
                "%H:%M"
            )

            self.label_horario.configure(
                text=f"Consulta realizada em: {horario}"
            )

        except:

            messagebox.showerror(
                "Erro",
                "Não foi possível conectar à internet!"
            )