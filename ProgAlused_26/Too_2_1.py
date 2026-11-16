from random import *
# 1 Juku kinno
# Programm küsib eesnime. Kui nimi on Juku, kuvatakse „Lähme Jukuga kinno!“, 
# muidu teatatakse, et täna kinno ei minda.
# Programm peab Juku ära tundma ka siis, 
# kui nimi on kirjutatud suurtähtedega (JUKU) või väiketähtedega (juku).
# Kui nimi on kirjutatud ainult suurtähtedega, 
# lisa märkus „Ära karju, Juku!“.
eesnimi=input("Sisesta eesnimi: ")
if eesnimi.upper()=="JUKU":
    print("Lähme Jukuga kinno!")
    if eesnimi.isupper():
        print("Ära karju, Juku!")
    elif eesnimi.islower():
        print("Ära sosista, Juku!")
    #Kui kinno läheb Juku, küsi tema vanus ja otsusta, millist piletit on vaja osta:
    try:
        vanus=int(input("Kui vana sa oled, Juku? "))
        if 0 <=vanus < 6:
            pilet="tasutapilet"
        elif 6 <= vanus <= 14:
            pilet="lastepilet"
        elif 14 < vanus < 65:
            pilet="täispilet"
        elif 65<=vanus<=100:
            pilet="sooduspilet"
        else:
            print("Viga andmetes.")
        try:
            print(f"Juku vanus on {vanus} aastat, seega on vaja osta {pilet}.")
        except NameError:
            print("Piletit ei saa määrata, kuna vanus on vale.")
    except ValueError:
        print("Palun sisesta oma vanus numbrina.")
else:
    print("Täna kinno ei minda.")

# 2 Pinginaabrid
# Küsi kahe inimese nimed. Kontrolli, kas mõlemad nimed koosnevad ainult tähtedest. 
# Kui jah, teata kasutajale, kas nad on täna pinginaabrid või mitte. 
# Kui mõnes nimes on numbreid või muid märke, kuva veateade.
# Otsusta ise, kuidas „pinginaabrid“ määratakse, 
# näiteks juhuslikult või nimede algustähtede järgi.
# Kasuta: isalpha(), capitalize()
# pinginaabrid=["Anna","Vika"]
# nimi1=input("Sisesta esimese inimese nimi: ")
# nimi2=input("Sisesta teise inimese nimi: ")
# if nimi1.isalpha() and nimi2.isalpha():
#     if nimi1.capitalize() in pinginaabrid and nimi2.capitalize() in pinginaabrid:
#         print(f"{nimi1} ja {nimi2} on täna pinginaabrid.")
#     else:
#         print(f"{nimi1} ja {nimi2} ei ole täna pinginaabrid.")
# else:
#     print("Viga: nimed peavad koosnema ainult tähtedest.")
# #otsing nimede algustähtede järgi
# valik=input("Kas soovid otsida nimede algustähtede järgi? (jah/ei): ").lower()
# otsing=False
# if valik=="jah":
#     algustäht=input("Sisesta algustäht: ").capitalize()
#     for nimi in pinginaabrid:
#         if nimi.startswith(algustäht):
#             print(f"{nimi} algab tähega {algustäht}.")
#             otsing=True
#     if not otsing:
#         print(f"Ühtegi nime, mis algab tähega {algustäht}, ei leitud.")

# else:
#     print("Otsingut ei tehta.")

# 3. Remont
# Küsi ristkülikukujulise toa pikkus ja laius ning arvuta põranda pindala.
# Seejärel küsi, kas kasutaja soovib remonti teha. 
# Kui vastus on jaatav, küsi ruutmeetri hind ja arvuta põranda vahetamise hind.
# Lisaküsimus: kas kasutaja teeb remondi ise või kasutab professionaali abi? 
# Professionaali puhul küsi ka töö hind ruutmeetri kohta ja arvuta remondi koguhind koos tööga.
# Kasuta: float(), lower() (vastuse „Jah“, „JAH“, „jah“ äratundmiseks), round()
# try:
#     pikkus=float(input("Sisesta toa pikkus meetrites: "))
#     laius=float(input("Sisesta toa laius meetrites: "))
#     pindala=pikkus*laius
#     print(f"Toa põranda pindala on {pindala} ruutmeetrit.")
#     valik=input("Kas soovid remonti teha? (jah/ei): ").lower()
#     if valik=="jah":
#         try:
#             rm_hind=float(input("Sisesta ruutmeetri hind: "))
#             hind=round(pindala*rm_hind,2)
#             print(f"Põranda vahetamise hind on {hind} eurot.")
#             valik=input("Kas tahad remonti teha ise? (jah/ei): ").lower()
#             if valik=="jah":
#                 print(f"Remonti teed ise, koguhind on {hind} eurot.")
#             elif valik=="ei":
#                 try:
#                     töö_hind=float(input("Sisesta töö hind ruutmeetri kohta: "))
#                     hind=round(hind+pindala*töö_hind,2)
#                     print(f"Remonti teeb professionaal, koguhind on {hind} eurot.")
#                 except ValueError:
#                     print("Viga: Palun sisesta numbriline väärtus töö hinna jaoks.")
#             else:
#                 print("Viga: Palun sisesta jah või ei.")
#         except ValueError:
#             print("Viga: Palun sisesta numbriline väärtus ruutmeetri hinna jaoks.")
#     else:
#         print("Remonti ei tehta.")
# except ValueError:
#     print("Viga: Palun sisesta numbrilised väärtused pikkuse ja laiuse jaoks.")

# 4. Allahindlus
# Küsi toote alghind. Kui alghind on üle 700 euro, arvuta hind 30% soodustusega. 
# Muul juhul jääb hind samaks. Kuva lõplik hind kahe komakohaga.

# 5. Temperatuur
# Küsi toatemperatuur ja teata, kas see on üle 18 kraadi (soovitatav toasoojus talvel). 
# Temperatuur võib olla ka negatiivne või kümnendarv, seega kontrolli sisendit try/except abil.

# 6. Pikkus
# Küsi inimese pikkus sentimeetrites ja teata, 
# kas ta on lühike, keskmise pikkusega või pikk. 
# Piirid pane ise paika ja kirjuta need programmi alguses kommentaarina.

# 7. Pikkus ja sugu
# Täienda ülesannet 6: küsi lisaks sugu. 
# Meestele ja naistele kehtivad erinevad piirid. 
# Tingimusplokid võivad olla üksteise sees.
# Sugu võib sisestada mis tahes kujul (M, m, mees, MEES). 
# Programm peab selle ära tundma.
# Kui sugu on sisestatud valesti, kuva veateade.
# Kasuta: pesastatud if-laused, lower()

# 8. Poes
# Küsi kasutajalt iga toote kohta eraldi, kas ta soovib seda osta: 
#     piim, sai, leib ja vähemalt kaks toodet veel.
# Toodete hinnad loo juhuslikult moodulist random, näiteks round(random.uniform(0.5, 3), 2).
# Kui kasutaja soovib toodet osta, küsi kogus. Kontrolli, et kogus on täisarv (isdigit()).
# Lõpus kuva tšekk: iga ostetud toote nimi, kogus, hind ja summa ning kõige all kogusumma.
# ilma tsüklita ja listita
summa=0
arve="Toode   Kogus   Hind    Kokku\n"
valik=input("Kas soovid osta piima? (jah/ei): ")
if valik.lower()=="jah":
    kogus=input("Kui palju piima soovid osta (täisarv): ")
    if kogus.isdigit():
        kogus=int(kogus)
        piim_hind=round(uniform(0.5, 3), 2)
        print(f"Piima hind on {piim_hind} eurot.")
        summa+=kogus*piim_hind
        print(f"Piima kogusumma on {kogus*piim_hind} eurot.")
        arve+=f"piim   {kogus}   {piim_hind}€    {kogus*piim_hind}€\n"
else:
    print("Selge: Piima ei taha")
print(f"Kogusumma on:{round(summa,2)} eurot.")


valik=input("Kas soovid osta sai? (jah/ei): ")
if valik.lower()=="jah":
    kogus=input("Kui palju sai soovid osta (täisarv): ")
    if kogus.isdigit():
        kogus=int(kogus)
        sai_hind=round(uniform(0.5, 3), 2)
        print(f"Sai hind on {sai_hind} eurot.")
        summa+=kogus*sai_hind
        print(f"Sai kogusumma on {round(kogus*sai_hind,2)} eurot.")
        arve+=f"sai   {kogus}   {round(sai_hind,2)}€    {round(kogus*sai_hind,2)}€\n"
print(f"Kogusumma on:{round(summa,2)} eurot.")
valik=input("Kas soovid osta leiba? (jah/ei): ")
if valik.lower()=="jah":
    kogus=input("Kui palju leiba soovid osta (täisarv): ")
    if kogus.isdigit():
        kogus=int(kogus)
        leib_hind=round(uniform(0.5, 3), 2)
        print(f"Leiva hind on {round(leib_hind,2)} eurot.")
        summa+=kogus*leib_hind
        print(f"Leiva kogusumma on {round(kogus*leib_hind,2)} eurot.")
        arve+=f"leib   {kogus}   {round(leib_hind,2)}€    {round(kogus*leib_hind,2)}€\n"
print(f"Kogusumma on:{round(summa,2)} eurot.")
# Lõpus kuva tšekk: iga ostetud toote nimi, kogus, hind ja summa ning kõige all kogusumma.
print("Arve NR: 0000")
print("--------------")
print(arve)