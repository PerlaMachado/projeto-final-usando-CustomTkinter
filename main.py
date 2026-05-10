import customtkinter as ctk
from login import LoginApp

# Configuração de aparência
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Janela principal
app = LoginApp()

# Executa o sistema
app.mainloop()