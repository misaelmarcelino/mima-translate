# Campo de texto para ser traduzido
# Campo de texto para a tradução
# Selecionar a linguagem de entrada
# Selecionar a linguagem de saída
# Botão para tradução


from tkinter import YES, Tk, ttk, Text, Button
from googletrans import Translator

translator = Translator()


def traduzir(evento=None):
    texto = entradaTexto.get('1.0', 'end')
    src = comboEntrada.get()
    dest = comboSaida.get()
    resultado = translator.translate(text=texto, src=src, dest=dest)

    traducaoTexto.configure(state='normal')
    traducaoTexto.delete('1.0', 'end')
    traducaoTexto.insert('1.0', resultado.text)
    traducaoTexto.configure(state='disabled')


# Criando janela com TKinter
janela = Tk()
janela.title('Mima Tradutor')

values = ['pt', 'es', 'en']

box = ttk.Frame(width=450,)

# Entrada de tradução
frameEntrada = ttk.Frame()
labelEntrada = ttk.Label(
    frameEntrada, text='Escolha o idioma: ', font=('Roboto', 15))
comboEntrada = ttk.Combobox(frameEntrada,
                            values=values,
                            font=('Roboto', 15))
comboEntrada.set('pt')

labelEntrada.grid(row=0, column=0, )
comboEntrada.grid(row=0, column=1)
frameEntrada.pack(padx=15, pady=10)

entradaTexto = Text(width=50, height=10, font=('Roboto', 15), pady=10, padx=5)
entradaTexto.pack(padx=10, fill='both', expand="yes")

# Saída da tradução
frameSaida = ttk.Frame()
labelSaida = ttk.Label(
    frameSaida, text='Traduzindo para: ', font=('Roboto', 15))
comboSaida = ttk.Combobox(frameSaida,
                          values=values,
                          font=('Roboto', 15))
comboSaida.set('en')

labelSaida.grid(row=0, column=0, )
comboSaida.grid(row=0, column=1)
frameSaida.pack(padx=15, pady=10)

traducaoTexto = Text(width=50,
                     height=10,
                     font=('Roboto', 15),
                     pady=10,
                     padx=5,
                     state='disabled'
                     )
traducaoTexto.pack(padx=10, fill='both', expand="YES")

btnTraduzir = Button(text='Traduzir!', font=('Roboto', 15), command=traduzir)
btnTraduzir.pack(fill='both', padx=10, pady=10)

janela.bind('<Return>', traduzir)

box.pack()
janela.mainloop()
