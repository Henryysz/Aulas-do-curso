from tkinter import *
def clicar():
    print('Fui clicado')
    texto['text'] = 'Você clicou no botão'
    texto['fg'] = 'purple'


janela = Tk()
janela.title('IN')

texto = Label(
    text='Minha primera janela',
    font=('Arial', 24),
    padx=50,
    pady=50
    )
texto.pack()

btn = Button(
    text='Dá uma clicada',
    font=('Arial', 18, 'bold'),
    command=clicar
    )
btn.pack()


janela.mainloop()