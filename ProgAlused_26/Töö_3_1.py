while True:
    print("Vali ülesanne:")
    print("1. Täisarvude loendamine")
    print("2. Naturaalarvude summa")
    print("3. Positiivsete arvude korrutis")
    print("4. Arvude ruudud")
    print("5. Negatiivsete arvude summa")
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
        for i in range(8):
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
    elif valik.lower() == 'q':
        print("Programmist väljumine...")
        break
    else:
        print("Viga: Palun sisesta number 1-5 või 'q' väljumiseks.")
