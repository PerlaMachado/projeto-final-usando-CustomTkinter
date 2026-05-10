import customtkinter as ctk
from tkinter import messagebox
from menu import MenuApp
import tema


USUARIO_PADRAO = "admin"
SENHA_PADRAO = "1234"


class LoginApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        # =========================
        # CONFIGURAÇÕES
        # =========================
        self.title("Sistema de Automação")
        self.geometry("400x350")
        self.resizable(False, False)

        # =========================
        # TEMA
        # =========================
        ctk.set_appearance_mode(
            tema.tema_atual
        )

        # =========================
        # TÍTULO
        # =========================
        self.label_titulo = ctk.CTkLabel(
            self,
            text="Tela de Login",
            font=("Segoe UI", 28, "bold")
        )

        self.label_titulo.pack(
            pady=30
        )

        # =========================
        # USUÁRIO
        # =========================
        self.entry_usuario = ctk.CTkEntry(
            self,
            placeholder_text="Usuário",
            width=260,
            height=40
        )

        self.entry_usuario.pack(
            pady=10
        )

        # =========================
        # SENHA
        # =========================
        self.entry_senha = ctk.CTkEntry(
            self,
            placeholder_text="Senha",
            show="*",
            width=260,
            height=40
        )

        self.entry_senha.pack(
            pady=10
        )

        # =========================
        # BOTÃO LOGIN
        # =========================
        self.botao_login = ctk.CTkButton(
            self,
            text="Entrar",
            width=260,
            height=42,
            command=self.verificar_login
        )

        self.botao_login.pack(
            pady=20
        )

        # =========================
        # SWITCH TEMA
        # =========================
        self.switch_tema = ctk.CTkSwitch(
            self,
            text="",
            width=50,
            command=self.mudar_tema
        )

        self.switch_tema.place(
            x=330,
            y=20
        )

        # Mantém posição do switch
        if tema.tema_atual == "dark":

            self.switch_tema.select()

    # ===================================
    # ALTERAR TEMA
    # ===================================
    def mudar_tema(self):

        if self.switch_tema.get() == 1:

            tema.tema_atual = "dark"

        else:

            tema.tema_atual = "light"

        ctk.set_appearance_mode(
            tema.tema_atual
        )

    # ===================================
    # LOGIN
    # ===================================
    def verificar_login(self):

        usuario = self.entry_usuario.get()

        senha = self.entry_senha.get()

        if (
            usuario == USUARIO_PADRAO
            and
            senha == SENHA_PADRAO
        ):

            messagebox.showinfo(
                "Sucesso",
                "Login realizado!"
            )

            self.withdraw()

            self.menu = MenuApp()

        else:

            messagebox.showerror(
                "Erro",
                "Usuário ou senha incorretos!"
            )


if __name__ == "__main__":

    app = LoginApp()

    app.mainloop()