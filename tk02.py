from tkinter import *


def pega_texto():
    label['text'] = f'Olá, {cx_texto.get().title()}'
    label['fg'] = '#1338BE'
    cx_texto.delete(0, 'end')

janela = Tk()

rotulo = Label(
    text='Digite algo',
    font=('Mabook', 32)
    )
rotulo.grid(row=0, column=0, padx=25, pady=15)

cx_texto = Entry(font=('Comic Sans', 32))
cx_texto.grid(row=0, column=1, padx=25, pady=15)

btn = Button(
    text='Capturar texto',
    font=('Arial', 24),
    command=pega_texto
    )
btn.grid(row=0, column=2, padx=25, pady=15)

btn_sair = Button(
    text='Sair',
    font=('Arial', 24),
    command=exit
)
btn_sair.grid(row=1, column=2, padx=25, pady=15, sticky=EW)

label = Label(text='-----', font=('Mabook', 32))
label.grid(row=1, column=0, columnspan=2)

if __name__ == '__main__':
    janela.mainloop()
