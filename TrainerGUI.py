__author__ = "Liam Thomas-Chollier"
__copyright__ = "Copyright (C) 2021 Liam Thomas-Chollier"
__license__ = "Public Domain"
__version__ = "1.0"
import random
from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
root.title("Base Trainer")
basedep = StringVar(root)
decitext = StringVar(root)
BinaText = StringVar(root)
HexaText = StringVar(root)
decicheck = StringVar(root)
Binacheck = StringVar(root)
Hexacheck = StringVar(root)
basedep.set("Decimal")
w = OptionMenu(root, basedep, "Decimal", "Binaire", "Hexa").grid(row=0, column=0)
num = 0
def binaire(n):return ('{:0b}'.format(n))
def hexar(n):return ('{:0x}'.format(n))
def decimal(number, base):return (int(number,base))
def gen():
    global num
    decicheck.set("")
    Binacheck.set("")
    Hexacheck.set("")
    num = random.randint(0,255)
    decitext.set("")
    BinaText.set("")
    HexaText.set("")
    if basedep.get() == "Decimal":
        decitext.set(num)
    elif basedep.get() == "Binaire":
        BinaText.set(binaire(num))
    elif basedep.get() == "Hexa":
        HexaText.set(str(hexar(num)))
    else:
        print("erreur")
def check(nb):
    global num
    if nb == 1:
        if num == int(decitext.get()):
            decicheck.set(u"\u2713")
        else:
            decicheck.set(u"\u2717")
    elif nb == 2:
        print(str(binaire(num)))
        if num == decimal(BinaText.get(),2):
            Binacheck.set(u"\u2713")
        else:
            Binacheck.set(u"\u2717")
    elif nb == 3:
        if str(hexar(num)) == str(HexaText.get()).lower():
            Hexacheck.set(u"\u2713")
        else:
            Hexacheck.set(u"\u2717")
    else:
        print("erreur")
Label(root, text="Decimal").grid(row=2)
Label(root, text="Binaire").grid(row=3)
Label(root, text="Hexa").grid(row=4)
dec = Entry(root,textvariable=decitext).grid(row=2, column=1)
bin = Entry(root,textvariable=BinaText).grid(row=3, column=1)
hex = Entry(root,textvariable=HexaText).grid(row=4, column=1)
Button(root, text='Start', command=gen).grid(row=0, column=1)
Button(root, text='verifier', command=lambda:check(1)).grid(row=2, column=2)
Button(root, text='verifier', command=lambda:check(2)).grid(row=3, column=2)
Button(root, text='verifier', command=lambda:check(3)).grid(row=4, column=2)
deci = Label(root, text="Decimal",textvariable=decicheck).grid(row=2, column=3)
bina = Label(root, text="Binaire",textvariable=Binacheck).grid(row=3, column=3)
hexa = Label(root, text="Hexa",textvariable=Hexacheck).grid(row=4, column=3)
root.mainloop()
