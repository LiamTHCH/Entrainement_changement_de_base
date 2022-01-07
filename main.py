__author__ = "Liam Thomas-Chollier"
__version__ = "1.0"
import random
base = [2,10,16]
dico = {2: [10, 16], 10: [2, 16], 16: [2, 10]}
def binaire(n):return ('{:0b}'.format(n))
def hexa(n):return ('{:0x}'.format(n))
def decimal(number, base):return (int(number,base))
def askhex(num):return hexa(num) == str(input("Nombre en Hexa :")).lower()
def askbin(num):return binaire(num) == str(input("Nombre en Binaire :")).lower()
def askdec(num):return num == int(input("Nombre en Decimal :"))
def ask(base):
    if base == 2:
        while not askbin(list[0]):
            print("raté reesayes")
        print("Bravo")
    elif base == 10:
        while not askdec(list[0]):
            print("raté reesayes")
        print("Bravo")
    elif base == 16:
        while not askhex(list[0]):
            print("raté reesayes")
        print("Bravo")
    else:
        print("Erreur de Base")
while True:
    basedep = 0
    list = []
    list.append(random.randint(0,255))
    list.append(str(binaire(list[0])))
    list.append(str(hexa(list[0])))
    while basedep not in base:
        basedep = int(input("Quelle base de depart (2,10,16): "))
        if basedep not in base:
            print("Base non prise en charge")
        if basedep == 2:
            print("nombre :",list[1])
            for item in dico[2]:
                ask(item)
        elif basedep == 10:
            print("nombre :", list[0])
            for item in dico[10]:
                ask(item)
        elif basedep == 16:
            print("nombre :", list[2])
            for item in dico[16]:
                ask(item)
        else:
            print("erreur")
            exit(2)
    print("Bravo vous avez fait : %s -> %s -> %s "%(list[0],list[1],list[2]))
