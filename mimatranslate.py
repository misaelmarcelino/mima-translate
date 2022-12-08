# Campo de texto para ser traduzido
# Campo de texto para a tradução
# Selecionar a linguagem de entrada
# Selecionar a linguagem de saída
# Botão para tradução


from tkinter import Tk, ttk
from googletrans import Translator

translator = Translator()

def traduzir():
    texto=''
    src='',
    dest=''
    
    resultado= translator.translate()
    print(resultado.text)
    return resultado
)




