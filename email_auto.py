import customtkinter as ctk
from tkinter import messagebox
from cores import cores
import tema


class EmailFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        # =========================
        # CORES
        # =========================
        c = cores()

        self.cor_card = c["card"]
        self.cor_texto = c["texto"]
        self.cor_botao = c["botao"]
        self.cor_hover = c["hover"]

        self.configure(fg_color="transparent")

        # =========================
        # TÍTULO
        # =========================
        self.label_titulo = ctk.CTkLabel(
            self,
            text="📧 Envio de E-mail",
            font=("Segoe UI", 28, "bold"),
            text_color=self.cor_texto
        )

        self.label_titulo.pack(pady=(20, 10))

        # =========================
        # CARD PRINCIPAL
        # =========================
        self.frame_card = ctk.CTkFrame(
            self,
            width=500,
            height=650,
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
            height=40
        )

        self.entry_destinatario.pack(pady=(30, 10))

        # =========================
        # ASSUNTO
        # =========================
        self.entry_assunto = ctk.CTkEntry(
            self.frame_card,
            placeholder_text="Digite o assunto",
            width=350,
            height=40
        )

        self.entry_assunto.pack(pady=10)

        # =========================
        # MENSAGEM 
        # =========================
        self.texto_mensagem = ctk.CTkTextbox(
            self.frame_card,
            width=350,
            height=160,
            corner_radius=12,
            font=("Segoe UI", 14),

            # fundo e texto dinâmico
            fg_color="#FFFFFF" if tema.tema_atual == "light" else "#2A2D3E",
            text_color="#111111" if tema.tema_atual == "light" else "#FFFFFF",

            # 🔥 BORDA PRETA NO CLARO
            border_width=1,
            border_color="#000000" if tema.tema_atual == "light" else "#3B3F55"
        )

        self.texto_mensagem.pack(pady=15)

        # =========================
        # BOTÃO ENVIAR
        # =========================
        self.botao_enviar = ctk.CTkButton(
            self.frame_card,
            text="Enviar E-mail",
            width=220,
            height=45,
            fg_color=self.cor_botao,
            hover_color=self.cor_hover,
            command=self.enviar_email
        )

        self.botao_enviar.pack(pady=15)

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

    # =========================
    # ENVIAR
    # =========================
    def enviar_email(self):

        dest = self.entry_destinatario.get()
        assunto = self.entry_assunto.get()
        msg = self.texto_mensagem.get("1.0", "end").strip()

        if not dest or not assunto or not msg:
            self.label_status.configure(
                text="Preencha todos os campos!",
                text_color="#EF4444"
            )
            return

        self.label_status.configure(
            text="E-mail enviado com sucesso! ✅",
            text_color="#22C55E"
        )

        self.entry_destinatario.delete(0, "end")
        self.entry_assunto.delete(0, "end")
        self.texto_mensagem.delete("1.0", "end")