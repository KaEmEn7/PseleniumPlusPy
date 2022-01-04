import string
import random

abc = list(string.ascii_letters)    #ulozit list a-Z do abc
email = ""                          #prazndy mail kam se napoji stringy z funkce
for i in range(7):                  #range 7 = 7 znaku+@testfeo.cz (7+11)
    if len(email) <= 20:            #kontrola ze email neni delsi jak 20 charů (7+11) podminka musí být splněna
        x = random.randint(0, 51)   #random znak 0-51 z abc listu vsech znaku abecedy
        n = abc[x]                  #do promenne n se ulozi jeden znak [x] z listu
        email = n + email           #spojeni znaku k sobě
x = (email)+"@testfeo.cz"           #do promenne x se uloží celý string random emailu
print(x)

phone = ""                          #prazdne cislo kam se napojí random cisla z nums
for i in range(9):                  #9x se pustí for cyklus = 9ti místné číslo
    x = random.randint(0, 9)        #do promenne x se ulozi random cislo 0-9
    phone = str(phone) + str(x)     #pretipovani cisel (int) na str aby se z nich dal spojit string
print(phone)
