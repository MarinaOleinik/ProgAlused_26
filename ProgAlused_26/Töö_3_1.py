
while True:
    print("""
          1. Täisarvude loendamine
          2. Naturaalarvude summa
          3. Positiivsete arvude korrutis
          4. Arvude ruudud
          5. Negatiivsete arvude summa
          6.Klaviatuurilt sisestatakse N arvu.
            Koosta programm, mis määrab sisestatud arvude seast:
            negatiivsete arvude arvu,
            positiivsete arvude arvu,
            nullide arvu.(N väärtus sisestatakse klaviatuurilt.)
          7. Väljastada ekraanile arvud, mis on K-ga jaguvad vahemikust [A, B].""")
    valik=input("Sisesta ülesande number (1-5) või 'q' väljumiseks: ")
    if valik == '1':
        # 1️
        # Sisestatakse 15 arvu.
        # Määrata, mitu neist on täisarvud.
        # while tingimustega tsükkel
        i = 0  # loendur
        kogus = 0  # täisarvude kogus
        while i < 15:
            arv = float(input(f"{i + 1}. arv: "))
            if arv.is_integer():
                kogus += 1
            i += 1
        print("Täisarve:", kogus)
    elif valik == '2':
        i = 0  # loendur
        kogus = 0  # naturaalarvude summa
        while i < 15:
            arv = float(input(f"{i + 1}. arv: "))
            if arv.is_integer() and arv > 0:
                kogus += arv
            i += 1
        print("Naturaalarvude summa:", kogus)
    elif valik == '3':
        # 3️
        # Sisestatakse 8 arvu.
        # Leida nende korrutis (ainult positiivsete arvude puhul).
        korrutis = 1
        for i in range(0,8,1):
            arv = float(input(f"{i + 1}. arv: "))
            if arv > 0:
                korrutis *= arv
        print("Korrutis:", korrutis)
    elif valik == '4':
        # 4️
        # Koosta programm, mis väljastab ekraanile arvude ruudud vahemikus 10 kuni 20.
        for i in range(10, 21):
            print(f"{i}^2 on {i ** 2}")
    elif valik == '5':
        # 5️
        # Koosta programm, mis arvutab ainult negatiivsete arvude summa N sisestatud arvu seast.
        # N väärtus sisestatakse klaviatuurilt.
        try:
            while True:
                N = int(input("Sisesta arv N > 0: "))
                if N > 0: break
            summa = 0
            for i in range(N):
                arv = float(input(f"{i + 1}. arv: "))
                if arv < 0:
                    summa += arv
            print("Negatiivsete arvude summa:", summa)

        except ValueError:
            print("Palun sisesta kehtiv täisarv.")
    elif valik == '6':
        pos_kogus=0
        neg_kogus=0
        null_kogus=0
        while True:
            try:
                N = int(input("Sisesta arv N > 0: "))
                if N > 0: break
            except ValueError:
                print("Palun sisesta kehtiv täisarv.")
                continue
        for i in range(N):
            while True:
                try:
                    arv = float(input(f"{i + 1}. arv: "))
                    break
                except ValueError:
                    print("Palun sisesta kehtiv arv.")
            if arv < 0:
                print("Negatiivne arv")
                neg_kogus += 1
            elif arv > 0:
                print("Positiivne arv")
                pos_kogus += 1
            else:
                print("Null")
                null_kogus += 1
        print(f"Negatiivsete arvude kogus: {neg_kogus}")
        print(f"Positiivsete arvude kogus: {pos_kogus}")
        print(f"Nullide kogus: {null_kogus}")
    elif valik == '7':
        while True:
            try:
                A = int(input("Sisesta arv A: "))
                B = int(input("Sisesta arv B: "))
                K = int(input("Sisesta arv K: "))#Tee K kontroll, et see ei oleks 0
                break
            except ValueError:
                print("Palun sisesta kehtiv täisarv.")
            if A>B:
                print("A peab olema väiksem või võrdne B-ga. Siis vahetame need.")
                A,B=B,A
        print(f"Arvud vahemikus [{A}, {B}], mis on {K}-ga jaguvad:")
        for i in range(A, B + 1):
            if i % K == 0:
                print(i)
    elif valik.lower() == 'q':
        print("Programmist väljumine...")
        break
#Iseseisev töö:
#Valige ükskõik millised 5 ülesannet, kirjutage kood, laadige see GitHubi üles ja lisage link ülesandele vastuseks.
    else:
        print("Viga: Palun sisesta number 1-5 või 'q' väljumiseks.")
