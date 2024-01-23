# Projeto do relogio

import tkinter as tk
from tkinter import *
import os
from time import strftime

root = tk.Tk()
root.title(" Relógio(:) ")
root.geometry("600x320")
root.maxsize(600, 320)
root.minsize(600, 320)
root.configure(background= '#86608E')

def get_nome():
    nomer_usuario = os.getlogin()
    nome.config(text=f'Bem vinda, {nomer_usuario}')

def get_data():
    data_atual = strftime('%a, %d/%m/%Y')
    data.config(text=data_atual)

def get_hora():
    hora_atual = strftime('%H:%M:%S')
    hora.config(text=hora_atual)
    hora.after(1000, get_hora)
    
margin = tk.Canvas(root, width=600, height=60, bg='#86608E', bd=0, highlightthickness=0, relief='ridge')
margin.pack()

nome= Label(root, bg='#86608E', fg='#000000', font=('Montserrat', 16))
nome.pack()

data= Label(root, bg='#86608E', fg='#000000', font=('Montserrat', 14))
data.pack(pady=2)

hora=Label(root, bg='#86608E', fg='#000000', font=('Montserrat', 64, 'bold'))
hora.pack(pady=2)





get_nome()
get_data()
get_hora()

root.mainloop()
