#Töö1.1
#Ülesanne 1
# Kirjuta enda esimene programm, mis väljastab käsureale teksti: 
#     “Tere, maailm!”. 
# Küsi kasutaja nimi ja muuda tekst, et ta näeks välja nii: 
#     “Tere, maailm! Tervitan sind Mati”, kui kasutaja nimi on Mati.
# Küsi kasutajalt sisend tema vanuse kohta ning väljasta see ekraanile:
# “Tere, maailm! Tervitan sind Mati! Sa oled N aastat vana.”



#Õpik punkt 1.14 try ... except plokk

print("Tere, maailm!")
nimi=input("Sisesta oma nimi: ")
print(f"Tere, maailm! Tervitan sind {nimi}!")
try:
    vanus=int(input("Sisesta oma vanus: ")) #int() teisendab stringi täisarvuks
    print(f"Tere, maailm! Tervitan sind {nimi}! Sa oled {vanus} aastat vana.")
except:
    print("Vale andmetüüp") #


#E-portfoolio
#Töö 1.3









#Ülesanne 2
# Mis tüüpi on järgnevad muutujad:
# a) vanus = 18
# b) eesnimi = "Jaak"
# c) pikkus = 16.5
# d) kas_käib_koolis = True
# Mis võimalus veel peale True oleks viimast muutujat väärtustada? 
# Kuidas võiks nende muutujate väärtusi koodis kontrollida?
# Kirjuta kood tüüpide kontrollimiseks.
vanus=18 #int
eesnimi="Jaak" #str
pikkus=165.5 #float
kas_käib_koolis=True #bool
print(f"Muutuja: {vanus}, tüüp: {type(vanus)}")
print(f"Muutuja: {eesnimi}, tüüp: {type(eesnimi)}")
print(f"Muutuja: {pikkus}, tüüp: {type(pikkus)}")
print(f"Muutuja: {kas_käib_koolis}, tüüp: {type(kas_käib_koolis)}")

#Ülesanne 3
# Kirjuta enda koodis laual olevate kommide arv muutujasse
# (kommide arv on juhuslik). 
# Seejärel kuva muutujas olev kommide arv ekraanile kasutades print() käsku.
# Küsi kasutajalt sisendit, mitu kommi ta soovib laualt ära võtta. 
# Eemalda soovitud kommide arv laual olevate kommide arvust ja kuva ekraanile, 
# kui palju komme laual nüüd on.
from random import * #randint
kommide_arv=randint(1,100) #kommide arv on juhuslik arv vahemikus 1-100)
print(f"Laual on {kommide_arv} kommi.")
try:
    kommid=int(input("Mitu kommi soovid laualt ära võtta? "))
    kommide_arv -= kommid #kommide_arv väheneb kommid võrra
    print(f"Laual on nüüd {kommide_arv} kommi.")
except:
    print("Sisesta arv")



#Ülesanne 4
# Puu läbimõõdu arvutamine
# Kirjuta programm, 
# mis küsib kasutaja käest puu ümbermõõdu 
# ning teatab selle peale puu läbimõõdu.
from math import * #pi,sqrt()
try:
    ümbermõõt=float(input("Sisesta puu ümbermõõt: ")) #teisendab stringi ujukomaarvuks
    läbimõõt=ümbermõõt/pi
    print(f"Puu läbimõõt on {läbimõõt}.")
except:
    print("Sisesta mingi arv")



#Ülesanne 5
# Arvutage Pythoni käsureal, kui pikk on ristkülikukujulise maatüki diagonaal, 
# mille mõõtmed on Nm x Mm. N ja M küsi kasutajalt.
N=float(input("Sisesta ristküliku 1. külje pikkus: "))
M=float(input("Sisesta ristküliku 2. külje pikkus: "))
d=sqrt(N**2+M**2)
print(f"Ristküliku diagonaal on {d}.")

#Ülesanne 6
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus/aeg

print("Sinu kiirus oli " + str(kiirus) + " km/h")

#Ülesanne 7
# Koostada programm, mis arvutab aritmeetilise keskmise 
# suvalisest etteantud 5 täis arvust.
# Leia nende arvude summa, jagatuna kasutaja poolt sisestatud arvuga, 
# täisarvuline osa ja jääk.
arv1=int(input("Sisesta 1. täisarv: "))
arv2=int(input("Sisesta 2. täisarv: "))
arv3=int(input("Sisesta 3. täisarv: "))
arv4=int(input("Sisesta 4. täisarv: "))
arv5=int(input("Sisesta 5. täisarv: "))
keskmine=(arv1+arv2+arv3+arv4+arv5)/5
summa=arv1+arv2+arv3+arv4+arv5
print(f"Arvude summa on {summa}.")
print(f"Arvude keskmine on {keskmine}.")
täisosa=summa//5
jääk=summa%5
print(f"Täisosa on {täisosa}.")
print(f"Jääk on {jääk}.")

#Ülesanne 9
a=int(input("Sisesta 1. täisarv: "))
b=int(input("Sisesta 2. täisarv: "))
c=int(input("Sisesta 3. täisarv: "))
P=a+b+c
