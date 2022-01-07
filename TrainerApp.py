__author__ = "Liam Thomas-Chollier"
__version__ = "1.0"
import random
from tkinter import *
from tkinter import ttk

class Trainer():
    def __init__(self):
        self.root = Tk()
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()
        self.root.title("Base Trainer")
        self.basedep = StringVar(self.root)
        self.decitext = StringVar(self.root)
        self.BinaText = StringVar(self.root)
        self.HexaText = StringVar(self.root)
        self.decicheck = StringVar(self.root)
        self.Binacheck = StringVar(self.root)
        self.Hexacheck = StringVar(self.root)
        self.basedep.set("Decimal")
        self.w = OptionMenu(self.root, self.basedep, "Decimal", "Binaire", "Hexa").grid(row=0, column=0)
        self.num = 0
        Label(self.root, text="Decimal").grid(row=2)
        Label(self.root, text="Binaire").grid(row=3)
        Label(self.root, text="Hexa").grid(row=4)
        self.dec = Entry(self.root, textvariable=self.decitext).grid(row=2, column=1)
        self.bin = Entry(self.root, textvariable=self.BinaText).grid(row=3, column=1)
        self.hex = Entry(self.root, textvariable=self.HexaText).grid(row=4, column=1)
        Button(self.root, text='Start', command=self.gen).grid(row=0, column=1)
        Button(self.root, text='verifier', command=lambda: self.check(1)).grid(row=2, column=2)
        Button(self.root, text='verifier', command=lambda: self.check(2)).grid(row=3, column=2)
        Button(self.root, text='verifier', command=lambda: self.check(3)).grid(row=4, column=2)
        deci = Label(self.root, text="Decimal", textvariable=self.decicheck).grid(row=2, column=3)
        bina = Label(self.root, text="Binaire", textvariable=self.Binacheck).grid(row=3, column=3)
        hexa = Label(self.root, text="Hexa", textvariable=self.Hexacheck).grid(row=4, column=3)
        self.root.mainloop()

    def check(self,nb):
        if nb == 1:
            if self.num == int(self.decitext.get()):
                self.decicheck.set(u"\u2713")
            else:
                self.decicheck.set(u"\u2717")
        elif nb == 2:
            if self.num == self.decimal(self.BinaText.get(),2):
                self.Binacheck.set(u"\u2713")
            else:
                self.Binacheck.set(u"\u2717")
        elif nb == 3:
            if str(self.hexar(self.num)) == str(self.HexaText.get()).lower():
                self.Hexacheck.set(u"\u2713")
            else:
                self.Hexacheck.set(u"\u2717")
        else:
            print("erreur")

    def gen(self):
        self.decicheck.set("")
        self.Binacheck.set("")
        self.Hexacheck.set("")
        self.num = random.randint(0, 255)
        self.decitext.set("")
        self.BinaText.set("")
        self.HexaText.set("")
        if self.basedep.get() == "Decimal":
            self.decitext.set(self.num)
        elif self.basedep.get() == "Binaire":
            self.BinaText.set(self.binaire(self.num))
        elif self.basedep.get() == "Hexa":
            self.HexaText.set(str(self.hexar(self.num)))
        else:
            print("erreur")

    def binaire(self,n):
        return ('{:0b}'.format(n))

    def hexar(self,n):
        return ('{:0x}'.format(n))

    def decimal(self,number, base):
        return (int(number, base))
app = Trainer()
