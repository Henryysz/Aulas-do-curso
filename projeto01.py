import mysql.connector
import os
from cores import *
from tkinter import *
from tkinter import messagebox
from dotenv import load_dotenv

load_dotenv('./env')
def conectar(event=None):
    try:
        conn = mysql.connector.connect(
            host=os.environ['host'],
            port=os.environ['port'],
            user=campo_nome.get(),
            passwd=campo_passwd.get(),
            db=os.environ['db']
        )
    except:
        campo_nome.delete(0, 'end')
        campo_passwd.delete(0, 'end')
        campo_nome.focus()
        messagebox.showerror(
            'Erro!',
            'Falha na conexão. Verifique se digitou o usuário ou senha corretamente.'
        )
    else:
        messagebox.showinfo(
            '100%',
            'Conexão realizada!'
        )

#Criando nossa janela
janela = Tk()
janela.title('')
janela.geometry('310x300')
janela.resizable(width=FALSE, height=FALSE)
janela.bind('<Return>', conectar)

#Dividindo em Frames
frame_superior = Frame(
    janela,
    width=310,
    height=50,
    bg=COR_IN
)
frame_superior.grid(
    row=0,
    column=0,
    padx=0,
    pady=1,
    sticky=NSEW
) 
frame_inferior = Frame(
    janela,
    width=310,
    height=250,
    bg=COR_FUNDO
)
frame_inferior.grid(
    row=1,
    column=0,
    padx=0,
    pady=1,
    sticky=NSEW
)

# Configurar o frame superior 
label = Label(
    frame_superior,
    text='Login',
    anchor=NW,
    font=('Small Fonts', 22),
    bg=COR_FUNDO,
    fg=COR_LETRA
)
label.place(x=5, y=-4)
linha = Label(
    frame_superior,
    width= 275,
    anchor=NW,
    bg=COR_IN
)
linha.place(x=20, y=48)

#Configurar o frame inferior
nome = Label(
    frame_inferior,
    text='Nome',
    anchor=NW,
    font=('Small Fonts', 14),
    bg=COR_FUNDO,
    fg=COR_LETRA
)
nome.place(x=10, y=20)
campo_nome = Entry(
    frame_inferior,
    width=28,
    justify='left',
    font=('Small Fonts', 14),
    highlightthickness=1,
    relief='solid'
)
campo_nome.place(x=10, y=50)
passwd = Label(
    frame_inferior,
    text='Senha',
    anchor=NW,
    font=('Small Fonts',14),
    bg=COR_FUNDO,
    fg=COR_LETRA
)
passwd.place(x=10, y=95)
campo_passwd = Entry(
    frame_inferior,
    width=28,
    justify='left',
    show='*',
    font=('Small Fonts', 14),
    highlightthickness=1,
    relief='solid'
)
campo_passwd.place(x=10, y=130)

btn_entrar = Button(
    frame_inferior,
    text='ENTRAR',
    font=('Small Fonts', 15),
    width=23,
    bg=COR_IN,
    fg=COR_FUNDO,
    command=conectar
)
btn_entrar.place(x=10, y=180)

if __name__ == '__main__':
    janela.mainloop()
