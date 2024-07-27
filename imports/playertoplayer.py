
from tkinter import *

def player2p() :

    global oneb,twob,threeb,fourb,fiveb,sixb,sevenb,eightb,nineb,w,sira,winner

    oneb = "N"

    twob = "N"

    threeb = "N"

    fourb = "N"

    fiveb = "N"

    sixb = "N"

    sevenb = "N"

    eightb = "N"

    nineb = "N"

    winner = None

    def ana_menu() :

        w.destroy()

    def tekrar_oyna() :

        w.destroy()

        player2p()

    def oyunbitti() :

        wi = Tk()
        wi.geometry("200x200+650+290")
        wi.config(background="#81F7F3")
        wi.title("XOX")
        wi.resizable(width=False,height=False)

        n = Label(wi)
        n.config(text=f"Game Over!\n\nWinner : {winner}",font=("Arial",18),bg="#81F7F3",fg="#2E2E2E")
        n.place(x=30,y=45)

        wi.after(2000, wi.destroy)

        wi.mainloop()

    def buttonr(no) :

        if no == "1" :

            one = Button(w)
            one.config(border=1,text=sira,font=("Arial",70),command=onep,bg="#15BDAC",fg="red")
            one.place(x=0,y=0,width=200,height=200)

        elif no == "2" :

            two = Button(w)
            two.config(border=1,text=sira,font=("Arial",70),bg="#15BDAC",fg="red",command=twop)
            two.place(x=0,y=200,width=200,height=200)

        elif no == "3" :

            three = Button(w)
            three.config(border=1,text=sira,font=("Arial",70),bg="#15BDAC",fg="red",command=threep)
            three.place(x=0,y=400,width=200,height=200)

        elif no == "4" :

            four = Button(w)
            four.config(border=1,text=sira,font=("Arial",70),bg="#15BDAC",fg="red",command=fourp)
            four.place(x=200,y=0,width=200,height=200)

        elif no == "5" :

            five = Button(w)
            five.config(border=1,text=sira,font=("Arial",70),bg="#15BDAC",fg="red",command=fivep)
            five.place(x=200,y=200,width=200,height=200)

        elif no == "6" :

            six = Button(w)
            six.config(border=1,text=sira,font=("Arial",70),bg="#15BDAC",fg="red",command=sixp)
            six.place(x=200,y=400,width=200,height=200)

        elif no == "7" :

            seven = Button(w)
            seven.config(border=1,text=sira,font=("Arial",70),bg="#15BDAC",fg="red",command=sevenp)
            seven.place(x=400,y=0,width=200,height=200)

        elif no == "8" :

            eight = Button(w)
            eight.config(border=1,text=sira,font=("Arial",70),bg="#15BDAC",fg="red",command=eightp)
            eight.place(x=400,y=200,width=200,height=200)

        elif no == "9" :

            nine = Button(w)
            nine.config(border=1,text=sira,font=("Arial",70),bg="#15BDAC",fg="red",command=ninep)
            nine.place(x=400,y=400,width=200,height=200)

    def hakem() :

        global winner

        liste = [(oneb,twob,threeb),(fourb,fiveb,sixb),(sevenb,eightb,nineb),(oneb,fourb,sevenb),(twob,fiveb,eightb),(threeb,sixb,nineb),(oneb,fiveb,nineb),(threeb,fiveb,sevenb)]

        for i in liste :

            i0 = i[0]

            i1 = i[1]

            i2 = i[2]

            if (i0[0]==i1[0]==i2[0]) and i0[0] != "N" :

                buttonr(i0[1])

                buttonr(i1[1])

                buttonr(i2[1])

                winner = i0[0]

                return True

            else :

                continue

        liste2 = [oneb,twob,threeb,fourb,fiveb,sixb,sevenb,eightb,nineb]

        try :

            while True :

                i = liste2[0]

                if i[0] == "N" :

                    break

                else :

                    liste2.remove(liste2[0])

                    continue

        except IndexError :

            wi = Tk()
            wi.geometry("200x200+650+290")
            wi.config(background="#81F7F3")
            wi.title("XOX")
            wi.resizable(width=False,height=False)

            n = Label(wi)
            n.config(text=f"Game Over!\n\n\nDraw",font=("Arial",18),background="#81F7F3")
            n.place(x=27,y=37)

            wi.after(2000, wi.destroy)

            wi.mainloop()

    sira = "X"

    def onep() :

        global sira, oneb,twob,threeb,fourb,fiveb,sixb,sevenb,eightb,nineb

        global sira, one,two,three,four,five,six,seven,eight,nine

        if oneb == "N" :

            if sira == "X" :

                xo = "#082A37"

            elif sira == "O" :

                xo = "#F1EBD3"

            one = Button(w)
            one.config(border=1,text=sira,font=("Arial",70),command=onep,bg="#15BDAC",fg=f"{xo}")
            one.place(x=0,y=0,width=200,height=200)

            oneb = sira+"1"

            if hakem() == True :

                oyunbitti()

            if sira == "X" :

                sira = "O"
            
            elif sira == "O" :

                sira = "X"

            siral = Label(w)
            siral.config(text=f"It's turn of {sira}",font=("Arial",20),bg="#15BDAC",fg="black")
            siral.place(x=220,y=615)

        else :

            pass

    def twop() :

        global sira, oneb,twob,threeb,fourb,fiveb,sixb,sevenb,eightb,nineb

        global sira, one,two,three,four,five,six,seven,eight,nine

        if twob == "N" :

            if sira == "X" :

                xo = "#082A37"

            elif sira == "O" :

                xo = "#F1EBD3"

            two = Button(w)
            two.config(border=1,text=sira,font=("Arial",70),bg="#15BDAC",fg=f"{xo}",command=twop)
            two.place(x=0,y=200,width=200,height=200)

            twob = sira+"2"

            if hakem() == True :

                oyunbitti()

            if sira == "X" :

                sira = "O"
            
            elif sira == "O" :

                sira = "X"

            siral = Label(w)
            siral.config(text=f"It's turn of {sira}",font=("Arial",20),bg="#15BDAC",fg="black")
            siral.place(x=220,y=615)

        else :

            pass

    def threep() :

        global sira, oneb,twob,threeb,fourb,fiveb,sixb,sevenb,eightb,nineb

        global sira, one,two,three,four,five,six,seven,eight,nine

        if threeb == "N" :

            if sira == "X" :

                xo = "#082A37"

            elif sira == "O" :

                xo = "#F1EBD3"

            three = Button(w)
            three.config(border=1,text=sira,font=("Arial",70),bg="#15BDAC",fg=f"{xo}",command=threep)
            three.place(x=0,y=400,width=200,height=200)

            threeb = sira+"3"

            if hakem() == True :

                oyunbitti()

            if sira == "X" :

                sira = "O"
            
            elif sira == "O" :

                sira = "X"

            siral = Label(w)
            siral.config(text=f"It's turn of {sira}",font=("Arial",20),bg="#15BDAC",fg="black")
            siral.place(x=220,y=615)

        else :

            pass

    def fourp() :

        global sira, oneb,twob,threeb,fourb,fiveb,sixb,sevenb,eightb,nineb

        global sira, one,two,three,four,five,six,seven,eight,nine

        if fourb == "N" :

            if sira == "X" :

                xo = "#082A37"

            elif sira == "O" :

                xo = "#F1EBD3"

            four = Button(w)
            four.config(border=1,text=sira,font=("Arial",70),bg="#15BDAC",fg=f"{xo}",command=fourp)
            four.place(x=200,y=0,width=200,height=200)

            fourb = sira+"4"

            if hakem() == True :

                oyunbitti()

            if sira == "X" :

                sira = "O"
            
            elif sira == "O" :

                sira = "X"

            siral = Label(w)
            siral.config(text=f"It's turn of {sira}",font=("Arial",20),bg="#15BDAC",fg="black")
            siral.place(x=220,y=615)

        else :

            pass

    def fivep() :

        global sira, oneb,twob,threeb,fourb,fiveb,sixb,sevenb,eightb,nineb

        global sira, one,two,three,four,five,six,seven,eight,nine

        if fiveb == "N" :

            if sira == "X" :

                xo = "#082A37"

            elif sira == "O" :

                xo = "#F1EBD3"

            five = Button(w)
            five.config(border=1,text=sira,font=("Arial",70),bg="#15BDAC",fg=f"{xo}",command=fivep)
            five.place(x=200,y=200,width=200,height=200)

            fiveb = sira+"5"

            if hakem() == True :

                oyunbitti()

            if sira == "X" :

                sira = "O"
            
            elif sira == "O" :

                sira = "X"

            siral = Label(w)
            siral.config(text=f"It's turn of {sira}",font=("Arial",20),bg="#15BDAC",fg="black")
            siral.place(x=220,y=615)

        else :

            pass

    def sixp() :

        global sira, oneb,twob,threeb,fourb,fiveb,sixb,sevenb,eightb,nineb

        global sira, one,two,three,four,five,six,seven,eight,nine

        if sixb == "N" :

            if sira == "X" :

                xo = "#082A37"

            elif sira == "O" :

                xo = "#F1EBD3"

            six = Button(w)
            six.config(border=1,text=sira,font=("Arial",70),bg="#15BDAC",fg=f"{xo}",command=sixp)
            six.place(x=200,y=400,width=200,height=200)

            sixb = sira+"6"

            if hakem() == True :

                oyunbitti()

            if sira == "X" :

                sira = "O"
            
            elif sira == "O" :

                sira = "X"

            siral = Label(w)
            siral.config(text=f"It's turn of {sira}",font=("Arial",20),bg="#15BDAC",fg="black")
            siral.place(x=220,y=615)

        else :

            pass

    def sevenp() :

        global sira, oneb,twob,threeb,fourb,fiveb,sixb,sevenb,eightb,nineb

        global sira, one,two,three,four,five,six,seven,eight,nine

        if sevenb == "N" :

            if sira == "X" :

                xo = "#082A37"

            elif sira == "O" :

                xo = "#F1EBD3"

            seven = Button(w)
            seven.config(border=1,text=sira,font=("Arial",70),bg="#15BDAC",fg=f"{xo}",command=sevenp)
            seven.place(x=400,y=0,width=200,height=200)

            sevenb = sira+"7"

            if hakem() == True :

                oyunbitti()

            if sira == "X" :

                sira = "O"
            
            elif sira == "O" :

                sira = "X"

            siral = Label(w)
            siral.config(text=f"It's turn of {sira}",font=("Arial",20),bg="#15BDAC",fg="black")
            siral.place(x=220,y=615)

        else :

            pass

    def eightp() :

        global sira, oneb,twob,threeb,fourb,fiveb,sixb,sevenb,eightb,nineb

        global sira, one,two,three,four,five,six,seven,eight,nine

        if eightb == "N" :

            if sira == "X" :

                xo = "#082A37"

            elif sira == "O" :

                xo = "#F1EBD3"

            eight = Button(w)
            eight.config(border=1,text=sira,font=("Arial",70),bg="#15BDAC",fg=f"{xo}",command=eightp)
            eight.place(x=400,y=200,width=200,height=200)

            eightb = sira+"8"

            if hakem() == True :

                oyunbitti()

            if sira == "X" :

                sira = "O"
            
            elif sira == "O" :

                sira = "X"

            siral = Label(w)
            siral.config(text=f"It's turn of {sira}",font=("Arial",20),bg="#15BDAC",fg="black")
            siral.place(x=220,y=615)

        else :

            pass

    def ninep() :

        global sira, oneb,twob,threeb,fourb,fiveb,sixb,sevenb,eightb,nineb

        global sira, one,two,three,four,five,six,seven,eight,nine

        if nineb == "N" :

            if sira == "X" :

                xo = "#082A37"

            elif sira == "O" :

                xo = "#F1EBD3"

            nine = Button(w)
            nine.config(border=1,text=sira,font=("Arial",70),bg="#15BDAC",fg=f"{xo}",command=ninep)
            nine.place(x=400,y=400,width=200,height=200)

            nineb = sira+"9"

            if hakem() == True :

                oyunbitti()

            if sira == "X" :

                sira = "O"
            
            elif sira == "O" :

                sira = "X"

            siral = Label(w)
            siral.config(text=f"It's turn of {sira}",font=("Arial",20),bg="#15BDAC",fg="black")
            siral.place(x=220,y=615)

        else :

            pass

    w = Tk()
    w.geometry("600x750+460+50")
    w.config(background="#15BDAC")
    w.title("XOX")
    w.resizable(width=False,height=False)

    one = Button(w)
    one.config(border=1,text="",font=("Arial",70),bg="#15BDAC",command=onep)
    one.place(x=0,y=0,width=200,height=200)

    two = Button(w)
    two.config(border=1,text="",font=("Arial",70),bg="#15BDAC",command=twop)
    two.place(x=0,y=200,width=200,height=200)

    three = Button(w)
    three.config(border=1,text="",font=("Arial",70),bg="#15BDAC",command=threep)
    three.place(x=0,y=400,width=200,height=200)

    four = Button(w)
    four.config(border=1,text="",font=("Arial",70),bg="#15BDAC",command=fourp)
    four.place(x=200,y=0,width=200,height=200)

    five = Button(w)
    five.config(border=1,text="",font=("Arial",70),bg="#15BDAC",command=fivep)
    five.place(x=200,y=200,width=200,height=200)

    six = Button(w)
    six.config(border=1,text="",font=("Arial",70),bg="#15BDAC",command=sixp)
    six.place(x=200,y=400,width=200,height=200)

    seven = Button(w)
    seven.config(border=1,text="",font=("Arial",70),bg="#15BDAC",command=sevenp)
    seven.place(x=400,y=0,width=200,height=200)

    eight = Button(w)
    eight.config(border=1,text="",font=("Arial",70),bg="#15BDAC",command=eightp)
    eight.place(x=400,y=200,width=200,height=200)

    nine = Button(w)
    nine.config(border=1,text="",font=("Arial",70),bg="#15BDAC",command=ninep)
    nine.place(x=400,y=400,width=200,height=200)

    siral = Label(w)
    siral.config(text=f"It's turn of {sira}",font=("Arial",20),bg="#15BDAC",fg="#2E2E2E")
    siral.place(x=220,y=615)

    anamenu = Button(w)
    anamenu.config(border=1,text="Main Menu",font=("Arial",20),command=ana_menu,bg="#81F7F3",fg="#2E2E2E")
    anamenu.place(x=100,y=675)

    tekrar = Button(w)
    tekrar.config(border=1,text="Play Again",font=("Arial",20),command=tekrar_oyna,bg="#81F7F3",fg="#2E2E2E")
    tekrar.place(x=340,y=675)

    w.mainloop()