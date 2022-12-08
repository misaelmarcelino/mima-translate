# Campo de texto para ser traduzido
# Campo de texto para a tradução
# Selecionar a linguagem de entrada
# Selecionar a linguagem de saída
# Botão para tradução


from tkinter import Tk, ttk, Text
from googletrans import Translator

translator = Translator()

def traduzir():
    texto=''
    src='',
    dest=''
    
    resultado= translator.translate()
    print(resultado.text)
    return resultado

# Criando janela com TKinter
janela = Tk()
janela.title('Mima Tradutor')

values = ['pt','es','en']

box = ttk.Frame(width=450, height=100,)
#Entrada de tradução
frameEntrada = ttk.Frame()
labelEntrada = ttk.Label(frameEntrada, text='Escolha o idioma de tradução: ', font=('Roboto', 15) )
comboEntrada = ttk.Combobox(frameEntrada, values=values, font=('Roboto', 15) )
comboEntrada.set('pt')
entradaTexto = Text(width=50, height=10)

labelEntrada.grid(row=0, column=0, )
comboEntrada.grid(row=0, column=1)
frameEntrada.pack(padx=15, pady=10)

entradaTexto.pack(padx=10, fill='both', expand='yes')

#Saída da tradução
frameSaida = ttk.Frame()
labelSaida = ttk.Label(frameSaida, text='Traduzir para: ') 
comboSaida = ttk.Combobox(frameSaida, values=values)
saidaTraducao = Text(height=10, width=50)

labelSaida.grid(row=0, column=0, )
comboSaida.grid(row=0, column=1)
frameSaida.pack( padx=10, pady=10)

saidaTraducao.pack(padx=10, fill='both', expand='yes')

box.pack()


janela.mainloop()



