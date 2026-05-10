import tema


def obter_cores():

    if tema.tema_atual == "dark":

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

            "texto": "black",

            "botao": "#3B82F6",

            "hover": "#2563EB"
        }