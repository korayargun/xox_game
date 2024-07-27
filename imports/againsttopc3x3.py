
from tkinter import *

import random

import threading

import time

def x2() :

    global ply,plyk,plyc,plykc

    ply = "X"

    plyk = "O"

    plyc = "#082A37"

    plykc = "#F1EBD3"

    w2.destroy()

    againstpc2()

def o2() :

    global ply,plyk,plyc,plykc

    ply = "O"

    plyk = "X"

    plyc = "#F1EBD3"

    plykc = "#082A37"

    w2.destroy()

    againstpc2()

def againstpc2() :

    global oneb,twob,threeb,fourb,fiveb,sixb,sevenb,eightb,nineb

    global x2,o2

    global one,two,three,four,five,six,seven,eight,nine,winner,ply,plyk,w

    oneb = "N1"

    twob = "N2"

    threeb = "N3"

    fourb = "N4"

    fiveb = "N5"

    sixb = "N6"

    sevenb = "N7"

    eightb = "N8"

    nineb = "N9"

    winner = "Berabere"

    def x2() :

        global ply,plyk,plyc,plykc

        ply = "X"

        plyk = "O"

        plyc = "#082A37"

        plykc = "#F1EBD3"

        w2.destroy()

        againstpc2()

    def o2() :

        global ply,plyk,plyc,plykc

        ply = "O"

        plyk = "X"

        plyc = "#F1EBD3"

        plykc = "#082A37"

        w2.destroy()

        againstpc2()

    def ist() :

        while True :

            print(f"1--{oneb} , 2--{twob} , 3--{threeb} , 4--{fourb} , 5--{fiveb} , 6--{sixb} , 7--{sevenb} , 8--{eightb} , 9--{nineb}")

    d1 = threading.Thread(target=ist)

    def ana_menu() :

        w.destroy()

    def tekrar_oyna() :

        w.destroy()

        againstpc()

    def oyunbitti() :

        global winner

        wi = Tk()
        wi.geometry("200x200+650+290")
        wi.config(background="#81F7F3")
        wi.title("XOX")
        wi.iconbitmap(default="icon.ico")
        wi.resizable(width=False,height=False)

        n = Label(wi)
        n.config(text=f"Game Over!\n\nWinner : {winner}",font=("Arial",18),bg="#81F7F3",fg="#2E2E2E")
        n.place(x=30,y=45)

        wi.after(2000, wi.destroy)

        wi.mainloop()

    def buttonr(xo,no) :

        global oneb,twob,threeb,fourb,fiveb,sixb,sevenb,eightb,nineb

        global one,two,three,four,five,six,seven,eight,nine

        print(no)

        if no == "1" :

            one = Button(w)
            one.config(border=1,text=f"{xo}",fg="red",bg="#15BDAC",font=("Arial",70),command=onep)
            one.place(x=0,y=0,width=200,height=200)

        elif no == "2" :

            two = Button(w)
            two.config(border=1,text=f"{xo}",fg="red",bg="#15BDAC",font=("Arial",70),command=twop)
            two.place(x=0,y=200,width=200,height=200)

        elif no == "3" :

            three = Button(w)
            three.config(border=1,text=f"{xo}",fg="red",bg="#15BDAC",font=("Arial",70),command=threep)
            three.place(x=0,y=400,width=200,height=200)

        elif no == "4" :

            four = Button(w)
            four.config(border=1,text=f"{xo}",fg="red",bg="#15BDAC",font=("Arial",70),command=fourp)
            four.place(x=200,y=0,width=200,height=200)

        elif no == "5" :

            five = Button(w)
            five.config(border=1,text=f"{xo}",fg="red",bg="#15BDAC",font=("Arial",70),command=fivep)
            five.place(x=200,y=200,width=200,height=200)

        elif no == "6" :

            six = Button(w)
            six.config(border=1,text=f"{xo}",fg="red",bg="#15BDAC",font=("Arial",70),command=sixp)
            six.place(x=200,y=400,width=200,height=200)

        elif no == "7" :

            seven = Button(w)
            seven.config(border=1,text=f"{xo}",fg="red",bg="#15BDAC",font=("Arial",70),command=sevenp)
            seven.place(x=400,y=0,width=200,height=200)

        elif no == "8" :

            eight = Button(w)
            eight.config(border=1,text=f"{xo}",fg="red",bg="#15BDAC",font=("Arial",70),command=eightp)
            eight.place(x=400,y=200,width=200,height=200)

        elif no == "9" :

            nine = Button(w)
            nine.config(border=1,text=f"{xo}",fg="red",bg="#15BDAC",font=("Arial",70),command=ninep)
            nine.place(x=400,y=400,width=200,height=200)

    def hakem() :

        global winner

        liste = [(oneb,twob,threeb),(fourb,fiveb,sixb),(sevenb,eightb,nineb),(oneb,fourb,sevenb),(twob,fiveb,eightb),(threeb,sixb,nineb),(oneb,fiveb,nineb),(threeb,fiveb,sevenb)]

        for i in liste :

            i0 = i[0]

            i1 = i[1]

            i2 = i[2]

            if (i0[0] == i1[0] == i2[0]) and (i0[0] != "N") :

                buttonr(i0[0],i0[1])

                buttonr(i1[0],i1[1])

                buttonr(i2[0],i2[1])

                winner = i0[0]

                return True
            
            else :

                continue

    def button(no) :

        global oneb,twob,threeb,fourb,fiveb,sixb,sevenb,eightb,nineb

        global one,two,three,four,five,six,seven,eight,nine

        print(no)

        if no == "1" :

            one = Button(w)
            one.config(border=1,text=f"{plyk}",fg=f"{plykc}",bg="#15BDAC",font=("Arial",70),command=onep)
            one.place(x=0,y=0,width=200,height=200)

            oneb = f"{plyk}1"

            if hakem() == True :

                oyunbitti()

            print(1)

        elif no == "2" :

            two = Button(w)
            two.config(border=1,text=f"{plyk}",fg=f"{plykc}",bg="#15BDAC",font=("Arial",70),command=twop)
            two.place(x=0,y=200,width=200,height=200)

            twob = f"{plyk}2"

            if hakem() == True :

                oyunbitti()

            print(2)

        elif no == "3" :

            three = Button(w)
            three.config(border=1,text=f"{plyk}",fg=f"{plykc}",bg="#15BDAC",font=("Arial",70),command=threep)
            three.place(x=0,y=400,width=200,height=200)

            threeb = f"{plyk}3"

            if hakem() == True :

                oyunbitti()

            print(3)

        elif no == "4" :

            four = Button(w)
            four.config(border=1,text=f"{plyk}",fg=f"{plykc}",bg="#15BDAC",font=("Arial",70),command=fourp)
            four.place(x=200,y=0,width=200,height=200)

            fourb = f"{plyk}4"

            if hakem() == True :

                oyunbitti()

            print(4)

        elif no == "5" :

            five = Button(w)
            five.config(border=1,text=f"{plyk}",fg=f"{plykc}",bg="#15BDAC",font=("Arial",70),command=fivep)
            five.place(x=200,y=200,width=200,height=200)

            fiveb = f"{plyk}5"

            if hakem() == True :

                oyunbitti()

            print(5)

        elif no == "6" :

            six = Button(w)
            six.config(border=1,text=f"{plyk}",fg=f"{plykc}",bg="#15BDAC",font=("Arial",70),command=sixp)
            six.place(x=200,y=400,width=200,height=200)

            sixb = f"{plyk}6"

            if hakem() == True :

                oyunbitti()

            print(6)

        elif no == "7" :

            seven = Button(w)
            seven.config(border=1,text=f"{plyk}",fg=f"{plykc}",bg="#15BDAC",font=("Arial",70),command=sevenp)
            seven.place(x=400,y=0,width=200,height=200)

            sevenb = f"{plyk}7"

            if hakem() == True :

                oyunbitti()

            print(7)

        elif no == "8" :

            eight = Button(w)
            eight.config(border=1,text=f"{plyk}",fg=f"{plykc}",bg="#15BDAC",font=("Arial",70),command=eightp)
            eight.place(x=400,y=200,width=200,height=200)

            eightb = f"{plyk}8"

            if hakem() == True :

                oyunbitti()

            print(8)

        elif no == "9" :

            nine = Button(w)
            nine.config(border=1,text=f"{plyk}",fg=f"{plykc}",bg="#15BDAC",font=("Arial",70),command=ninep)
            nine.place(x=400,y=400,width=200,height=200)

            nineb = f"{plyk}9"

            if hakem() == True :

                oyunbitti()

            print(9)

        else :

            print("Hata button",no)

    def hamle() :

        global oneb,twob,threeb,fourb,fiveb,sixb,sevenb,eightb,nineb,ply,plyk

        global one,two,three,four,five,six,seven,eight,nine

        liste = [(oneb,twob,threeb),(fourb,fiveb,sixb),(sevenb,eightb,nineb),(oneb,fourb,sevenb),(twob,fiveb,eightb),(threeb,sixb,nineb),(oneb,fiveb,nineb),(threeb,fiveb,sevenb)]

        for i in liste :

            i0 = i[0]

            i1 = i[1]

            i2 = i[2]

            if (i0[0] == i1[0] == f"{plyk}") and i2[0] == "N" :

                button(i2[1])

                print(10)

                break

            elif (i0[0] == i2[0] == f"{plyk}") and i1[0] == "N" :

                button(i1[1])

                print(11)

                break

            elif (i1[0] == i2[0] == f"{plyk}") and i0[0] == "N" :

                button(i0[1])

                print(12)

                break

            else :

                continue

        else :

            print("OO yok")

            liste = [(oneb,twob,threeb),(fourb,fiveb,sixb),(sevenb,eightb,nineb),(oneb,fourb,sevenb),(twob,fiveb,eightb),(threeb,sixb,nineb),(oneb,fiveb,nineb),(threeb,fiveb,sevenb)]

            for i in liste :

                i0 = i[0]

                i1 = i[1]

                i2 = i[2]

                if (i0[0] == i1[0] == f"{ply}") and i2[0] == "N" :

                    button(i2[1])

                    print(13)

                    break

                elif (i0[0] == i2[0] == f"{ply}") and i1[0] == "N" :

                    button(i1[1])

                    print(14)

                    break

                elif (i1[0] == i2[0] == f"{ply}") and i0[0] == "N" :

                    button(i0[1])

                    print(15)

                    break

                else :

                    continue

            else :

                print("XX yok")

                liste = [(oneb,twob,threeb),(fourb,fiveb,sixb),(sevenb,eightb,nineb),(oneb,fourb,sevenb),(twob,fiveb,eightb),(threeb,sixb,nineb),(oneb,fiveb,nineb),(threeb,fiveb,sevenb)]

                for i in liste :

                    i0 = i[0]

                    i1 = i[1]

                    i2 = i[2]

                    if ((i0[0] == f"{plyk}") or (i1[0] == f"{plyk}")) and ((i0[0] != f"{ply}") and (i1[0] != f"{ply}")) and i2[0] == "N" :

                        button(i2[1])

                        print(20)

                        break

                    elif ((i0[0] == f"{plyk}") or (i2[0] == f"{plyk}")) and ((i0[0] != f"{ply}") and (i2[0] != f"{ply}")) and i1[0] == "N" :

                        button(i1[1])

                        print(21)

                        break

                    elif ((i1[0] == f"{plyk}") or (i2[0] == f"{plyk}")) and ((i1[0] != f"{ply}") and (i2[0] != f"{ply}")) and i0[0] == "N" :

                        button(i0[1])

                        print(22)

                        break

                else :

                    print("O yok")

                    if (fiveb == "X5") and (oneb[0] or threeb[0] or sevenb[0] or nineb[0]) == "N" :

                        liste = ["1","3","7","9"]

                        secim = random.choice(liste)

                        button(secim)

                        print(16)

                    else :

                        print("5 yok")  

                        liste = [oneb,threeb,fiveb,sevenb,nineb]

                        if (oneb[0] == "N") or (threeb[0] == "N") or (fiveb[0] == "N") or (sevenb[0] == "N") or (nineb[0] == "N") :

                            while True :

                                try :

                                    i = random.choice(liste)

                                    if i[0] == "N" :

                                        button(i[1])

                                        print(23)

                                        break

                                    else :

                                        liste.remove(i)

                                        continue

                                except IndexError :

                                    break

                        else :

                            liste2 = [twob,fourb,sixb,eightb]

                            a = None

                            while True :

                                try :

                                    i = random.choice(liste2)

                                    if i[0] == "N" :

                                        button(i[1])

                                        print(24)

                                        break

                                    else :

                                        liste2.remove(i)

                                        continue

                                except IndexError :

                                    a = True

                                    break

                            if a == True :

                                wi = Tk()
                                wi.geometry("200x200+650+290")
                                wi.config(background="#81F7F3")
                                wi.title("XOX")
                                wi.iconbitmap(default="icon.ico")
                                wi.resizable(width=False,height=False)

                                n = Label(wi)
                                n.config(text=f"Game Over!\n\n\nDraw",font=("Arial",18),background="#81F7F3")
                                n.place(x=27,y=37)

                                wi.after(1000, wi.destroy)

                                wi.mainloop()

    def onep() :

        global oneb,twob,threeb,fourb,fiveb,sixb,sevenb,eightb,nineb

        if oneb == "N1" :

            one = Button(w)
            one.config(border=1,text=f"{ply}",fg=f"{plyc}",bg="#15BDAC",font=("Arial",70),command=onep)
            one.place(x=0,y=0,width=200,height=200)

            oneb = f"{ply}1"

            print("One geldi")

            if hakem() == True :

                oyunbitti()

            hamle()

            print("Hamle yapıldı one")

        else :

            print("Zaten var one")

    def twop() :

        global oneb,twob,threeb,fourb,fiveb,sixb,sevenb,eightb,nineb

        if twob == "N2" :

            two = Button(w)
            two.config(border=1,text=f"{ply}",fg=f"{plyc}",bg="#15BDAC",font=("Arial",70),command=twop)
            two.place(x=0,y=200,width=200,height=200)

            twob = f"{ply}2"

            print("Two geldi")

            if hakem() == True :

                oyunbitti()

            hamle()

            print("Hamle yapıldı two")

        else : 

            print("Zaten var two")

    def threep() :

        global oneb,twob,threeb,fourb,fiveb,sixb,sevenb,eightb,nineb

        if threeb == "N3" :

            three = Button(w)
            three.config(border=1,text=f"{ply}",fg=f"{plyc}",bg="#15BDAC",font=("Arial",70),command=threep)
            three.place(x=0,y=400,width=200,height=200)

            threeb = f"{ply}3"

            print("Three geldi")

            if hakem() == True :

                oyunbitti()

            hamle()

            print("Hamle yapıldı three")

        else : 

            print("Zaten var three")

    def fourp() :

        global oneb,twob,threeb,fourb,fiveb,sixb,sevenb,eightb,nineb

        if fourb == "N4" :

            four = Button(w)
            four.config(border=1,text=f"{ply}",fg=f"{plyc}",bg="#15BDAC",font=("Arial",70),command=fourp)
            four.place(x=200,y=0,width=200,height=200)

            fourb = f"{ply}4"

            print("Four geldi")

            if hakem() == True :

                oyunbitti()

            hamle()

            print("Hamle yapıldı four")
        else : 

            print("Zaten var four")

    def fivep() :

        global oneb,twob,threeb,fourb,fiveb,sixb,sevenb,eightb,nineb

        if fiveb == "N5" :

            five = Button(w)
            five.config(border=1,text=f"{ply}",fg=f"{plyc}",bg="#15BDAC",font=("Arial",70),command=fivep)
            five.place(x=200,y=200,width=200,height=200)

            fiveb = f"{ply}5"

            print("Five geldi")

            if hakem() == True :

                oyunbitti()

            hamle()

            print("hamle yapıldı five")

        else : 

            print("Zaten var five")

    def sixp() :

        global oneb,twob,threeb,fourb,fiveb,sixb,sevenb,eightb,nineb

        if sixb == "N6" :

            six = Button(w)
            six.config(border=1,text=f"{ply}",fg=f"{plyc}",bg="#15BDAC",font=("Arial",70),command=sixp)
            six.place(x=200,y=400,width=200,height=200)

            sixb = f"{ply}6"

            print("Six geldi")

            if hakem() == True :

                oyunbitti()

            hamle()

            print("Hamle yapıldı six")

        else : 

            print("Zaten var six")

    def sevenp() :

        global oneb,twob,threeb,fourb,fiveb,sixb,sevenb,eightb,nineb

        if sevenb == "N7" :

            seven = Button(w)
            seven.config(border=1,text=f"{ply}",fg=f"{plyc}",bg="#15BDAC",font=("Arial",70),command=sevenp)
            seven.place(x=400,y=0,width=200,height=200)

            sevenb = f"{ply}7"

            print("Seven geldi")

            if hakem() == True :

                oyunbitti()

            hamle()

            print("Hamle yapıldı seven")

        else : 

            print("Zaten var seven")

    def eightp() :

        global oneb,twob,threeb,fourb,fiveb,sixb,sevenb,eightb,nineb

        if eightb == "N8" : 

            eight = Button(w)
            eight.config(border=1,text=f"{ply}",fg=f"{plyc}",bg="#15BDAC",font=("Arial",70),command=eightp)
            eight.place(x=400,y=200,width=200,height=200)

            eightb = f"{ply}8"

            print("Eight geldi")

            if hakem() == True :

                oyunbitti()

            hamle()

            print("Hamle yapıldı eight")

        else : 

            print("Zaten var eight")

    def ninep() :

        global oneb,twob,threeb,fourb,fiveb,sixb,sevenb,eightb,nineb

        if nineb == "N9" : 

            nine = Button(w)
            nine.config(border=1,text=f"{ply}",fg=f"{plyc}",bg="#15BDAC",font=("Arial",70),command=ninep)
            nine.place(x=400,y=400,width=200,height=200)

            nineb = f"{ply}9"

            print("Nine geldi")

            if hakem() == True :

                oyunbitti()

            hamle()

            print("Hamle yapıldı nine")

        else : 

            print("Zaten var nine")

    w = Tk()
    w.geometry("600x700+460+50")
    w.config(background="#15BDAC")
    w.title("XOX")
    w.iconbitmap(default="icon.ico")
    w.resizable(width=False,height=False)

    one = Button(w)
    one.config(border=1,text="",font=("Arial",70),command=onep,bg="#15BDAC")
    one.place(x=0,y=0,width=200,height=200)

    two = Button(w)
    two.config(border=1,text="",font=("Arial",70),command=twop,bg="#15BDAC")
    two.place(x=0,y=200,width=200,height=200)

    three = Button(w)
    three.config(border=1,text="",font=("Arial",70),command=threep,bg="#15BDAC")
    three.place(x=0,y=400,width=200,height=200)

    four = Button(w)
    four.config(border=1,text="",font=("Arial",70),command=fourp,bg="#15BDAC")
    four.place(x=200,y=0,width=200,height=200)

    five = Button(w)
    five.config(border=1,text="",font=("Arial",70),command=fivep,bg="#15BDAC")
    five.place(x=200,y=200,width=200,height=200)

    six = Button(w)
    six.config(border=1,text="",font=("Arial",70),command=sixp,bg="#15BDAC")
    six.place(x=200,y=400,width=200,height=200)

    seven = Button(w)
    seven.config(border=1,text="",font=("Arial",70),command=sevenp,bg="#15BDAC")
    seven.place(x=400,y=0,width=200,height=200)

    eight = Button(w)
    eight.config(border=1,text="",font=("Arial",70),command=eightp,bg="#15BDAC")
    eight.place(x=400,y=200,width=200,height=200)

    nine = Button(w)
    nine.config(border=1,text="",font=("Arial",70),command=ninep,bg="#15BDAC")
    nine.place(x=400,y=400,width=200,height=200)

    anamenu = Button(w)
    anamenu.config(border=1,text="Main Menu",font=("Arial",20),command=ana_menu,fg="#2E2E2E",bg="#81F7F3")
    anamenu.place(x=100,y=630)

    tekrar = Button(w)
    tekrar.config(border=1,text="Play Again",font=("Arial",20),command=tekrar_oyna,fg="#2E2E2E",bg="#81F7F3")
    tekrar.place(x=340,y=630)

    w.mainloop()

def againstpc() :

    global w2,x2,o2

    w2 = Tk()
    w2.geometry("300x250+610+250")
    w2.config(background="#81F7F3")
    w2.title("XOX")
    w2.iconbitmap(default="icon.ico")
    w2.resizable(width=False,height=False)

    la = Label(w2)
    la.config(text="\nChoose your character :",font=("Arial",18),bg="#81F7F3",fg="#2E2E2E")
    la.pack(side=TOP)

    x = Button(w2)
    x.config(text="X",font=("Arial",28),border=1,command=x2,bg="#15BDAC",fg="#082A37")
    x.place(x=55,y=100,width=80,height=80)

    o = Button(w2)
    o.config(text="O",font=("Arial",28),border=1,command=o2,bg="#15BDAC",fg="#F1EBD3")
    o.place(x=165,y=100,width=80,height=80)

    w2.mainloop()