import customtkinter as ctk


class EmailFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        # =========================
        # CORES
        # =========================
        self.cor_fundo = "#1E1E2E"
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
            text="📧 Envio de E-mail",
            font=("Segoe UI", 28, "bold"),
            text_color="white"
        )

        self.label_titulo.pack(
            pady=(20, 20)
        )

        # =========================
        # CARD PRINCIPAL
        # =========================
        self.frame_card = ctk.CTkFrame(
            self,
            width=500,
            height=720,
            fg_color=self.cor_card,
            corner_radius=20
        )

        self.frame_card.pack(pady=10)

        self.frame_card.pack_propagate(False)

        # =========================
        # DESTINATÁRIO
        # =========================
        self.entry_destinatario = ctk.CTkEntry(
            self.frame_card,
            placeholder_text="Digite o e-mail do destinatário",
            width=350,
            height=40,
            corner_radius=12
        )

        self.entry_destinatario.pack(
            pady=(30, 15)
        )

        # =========================
        # ASSUNTO
        # =========================
        self.entry_assunto = ctk.CTkEntry(
            self.frame_card,
            placeholder_text="Digite o assunto",
            width=350,
            height=40,
            corner_radius=12
        )

        self.entry_assunto.pack(
            pady=15
        )

        # =========================
        # MENSAGEM
        # =========================
        self.texto_mensagem = ctk.CTkTextbox(
            self.frame_card,
            width=350,
            height=140,
            corner_radius=12,
            font=("Segoe UI", 14)
        )

        self.texto_mensagem.pack(
            pady=15
        )

        # =========================
        # BOTÃO ENVIAR
        # =========================
        self.botao_enviar = ctk.CTkButton(
            self.frame_card,
            text="Enviar E-mail",
            width=220,
            height=45,
            corner_radius=12,
            fg_color=self.cor_botao,
            hover_color=self.cor_hover,
            font=("Segoe UI", 15, "bold"),
            command=self.enviar_email
        )

        self.botao_enviar.pack(
            pady=20
        )

        # =========================
        # STATUS
        # =========================
        self.label_status = ctk.CTkLabel(
            self.frame_card,
            text="",
            font=("Segoe UI", 14),
            text_color="#B0B3C0"
        )

        self.label_status.pack()

    # ===================================
    # ENVIAR E-MAIL
    # ===================================
    def enviar_email(self):

        destinatario = self.entry_destinatario.get()

        assunto = self.entry_assunto.get()

        mensagem = self.texto_mensagem.get(
            "1.0",
            "end"
        ).strip()

        # Validação
        if (
            destinatario == ""
            or assunto == ""
            or mensagem == ""
        ):

            self.label_status.configure(
                text="Preencha todos os campos!",
                text_color="#EF4444"
            )

            return

        # Simulação visual
        self.label_status.configure(
            text="E-mail enviado com sucesso! ✅",
            text_color="#22C55E"
        )

        # Limpar campos
        self.entry_destinatario.delete(0, "end")

        self.entry_assunto.delete(0, "end")

        self.texto_mensagem.delete(
            "1.0",
            "end"
        )