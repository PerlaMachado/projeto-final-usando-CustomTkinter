import tema

def cores():
    modo = getattr(tema, "tema_atual", "light")

    if modo.lower() == "dark":
        return {
            "fundo": "#1E1E2E",
            "sidebar": "#181825",
            "card": "#2A2D3E",
            "texto": "white",
            "botao": "#3B82F6",
            "hover": "#2563EB"
        }
    else:
        return {
            "fundo": "#F3F4F6",
            "sidebar": "#E5E7EB",
            "card": "#FFFFFF",
            "texto": "#0D0D0D",
            "botao": "#3B82F6",
            "hover": "#2563EB"
        }