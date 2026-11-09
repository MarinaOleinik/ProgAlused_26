#Lihtne if



x = -5 # testimiseks kirjuta siia mõni arv
try:
    x=int(input("Sisesta täisarv: "))
    if x > 0:
        print("Positiivne arv")
        print("See rida on ka if-i sees")
    print("See rida täidetakse alati")
except ValueError:
    print("Palun sisesta kehtiv täisarv.")

#if else
try:
    x = int(input("Sisesta arv: "))
    if x == 1:
        print("Õige")
    else:
        print("Vale")
except ValueError:
    print("Palun sisesta kehtiv täisarv.")

vastus = input("Kas soovid jätkata? (jah/ei) ")
print("Sinu vastus oli:", vastus)
# vastuse_tüüp=type(vastus)
# print("Vastuse tüüp on:",vastuse_tüüp) #<class 'str'>
# kas_vastus_on_tekst=vastus.isalpha() #kontrollib, kas vastus on tekst
# print("Kas see on tekst:",kas_vastus_on_tekst) #True või False
if vastus.isalpha():
    if vastus.lower() == "jah":
        print("Jätkame!")
    else:
        print("Head aega!")
else:
    print("Palun sisesta 'jah' või 'ei'.")

#if ... elif... else
try:  
    x = int(input("Sisesta arv -5 kuni 5: "))
    if x < -5:
        print("Vähe")
    elif -5 <= x <= 5:
        print("OK")
    else:
        print("Palju")
except:
    print("Palun sisesta kehtiv täisarv.")
# if on if'i sees
#Muuda kood nii, et räägime kasutajaga ainult siis, 
#kui tema nimi on ainult tähed ja esimene täht on suur
nimi = input("Sisesta nimi: ")
print("Ainult tähed:", nimi.isalpha())
print("Suurtähtedega:", nimi.isupper())
print("Algab suurtähega:", nimi.istitle())
if nimi.isalpha() and nimi.istitle():
    print("Nimi sobib.")
    try:
        vanus = int(input(f"{nimi} Kui vana sa oled? "))
        if vanus >= 18:
            juhiluba = input(f"{nimi}. Kas sul on juhiluba? (jah/ei) ")
            if juhiluba.lower() == "jah":
                print("Võid autot juhtida.")
            elif juhiluba.lower() == "ei":
                print("Kõigepealt tee juhiload.")
            else:
                print(f"Ära vasta {juhiluba}. Vasta jah või ei.")
        else:
            print("Oled autojuhtimiseks liiga noor.")
    except:
        print("Palun sisesta kehtiv täisarv.")
else:
    print("Nimes tohib olla ainult tähti!")
