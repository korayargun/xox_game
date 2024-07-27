
"""

Writer : Koray ARGÜN

Date : 24.01.2023

"""

from tkinter import *

import random

import threading

from imports.againsttopc3x3 import againstpc

from imports.playertoplayer import player2p

def pcp() :

    wi2.destroy()

    print("pcpye gelindi")

    againstpc()

    print("againsttopc imported")

    main()

def p2p() :

    wi2.destroy()

    print("p2pye gelindi")

    player2p()

    print("playertoplayer imported")

    main()

def main() :

    global wi2

    wi2 = Tk()
    wi2.title("Tic-Tac-Toe")
    wi2.geometry("250x250+630+250")
    wi2.config(background="#15BDAC")
    wi2.iconbitmap(default="icon.ico")
    wi2.resizable(width=False,height=False)

    label = Label(wi2)
    label.config(text="\nXOX\n\nWelcome!",background="#15BDAC",font=40)
    label.pack(side=TOP)

    pc = Button(wi2)
    pc.config(text="Against To PC",font=40,border=1,fg="#2E2E2E",bg="#81F7F3",command=pcp)
    pc.place(x=55,y=130)

    player = Button(wi2)
    player.config(text="Two Player",font=40,border=1,fg="#2E2E2E",bg="#81F7F3",command=p2p)
    player.place(x=70,y=190)

    wi2.mainloop()

main()