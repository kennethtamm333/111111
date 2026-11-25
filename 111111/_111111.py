import random
 
 
# 7. Arvud, mis jaguvad K-ga vahemikus [A, B]
def ülesanne_7(t):
    A = int(input("Sisesta A: "))
    B = int(input("Sisesta B: "))
    K = int(input("Sisesta K: "))
 
    if t == "1":
        for arv in range(A, B + 1):
            if arv % K == 0:
                print(arv)
    elif t == "2":
        arv = A
        while arv <= B:
            if arv % K == 0:
                print(arv)
            arv += 1
    else:
        arv = A
        while True:
            if arv > B:
                break
            if arv % K == 0:
                print(arv)
            arv += 1
 
 
# 8. Tollide ja sentimeetrite tabel (1 toll = 2,5 cm), 1 kuni 20 tolli
def ülesanne_8(t):
    print("Tolli | Sentimeetrit")
 
    if t == "1":
        for toll in range(1, 21):
            print(toll, "|", toll * 2.5)
    elif t == "2":
        toll = 1
        while toll <= 20:
            print(toll, "|", toll * 2.5)
            toll += 1
    else:
        toll = 1
        while True:
            if toll > 20:
                break
            print(toll, "|", toll * 2.5)
            toll += 1
 
 
# 9. Pangas S eurot, 3% intress, summa N aasta pärast
def ülesanne_9(t):
    S = float(input("Sisesta algsumma (eurot): "))
    N = int(input("Sisesta aastate arv: "))
    summa = S
 
    if t == "1":
        for aasta in range(1, N + 1):
            summa = summa * 1.03
            print("Aasta", aasta, ":", round(summa, 2), "eurot")
    elif t == "2":
        aasta = 1
        while aasta <= N:
            summa = summa * 1.03
            print("Aasta", aasta, ":", round(summa, 2), "eurot")
            aasta += 1
    else:
        aasta = 1
        while True:
            if aasta > N:
                break
            summa = summa * 1.03
            print("Aasta", aasta, ":", round(summa, 2), "eurot")
            aasta += 1
 
    print("Summa", N, "aasta pärast:", round(summa, 2), "eurot")
 
 
# 10. 10 arvupaari, väljasta igast paarist suurem
def ülesanne_10(t):
    if t == "1":
        for i in range(10):
            a = float(input("Sisesta esimene arv: "))
            b = float(input("Sisesta teine arv: "))
            if a > b:
                print("Suurem:", a)
            elif b > a:
                print("Suurem:", b)
            else:
                print("Arvud on võrdsed")
    elif t == "2":
        i = 0
        while i < 10:
            a = float(input("Sisesta esimene arv: "))
            b = float(input("Sisesta teine arv: "))
            if a > b:
                print("Suurem:", a)
            elif b > a:
                print("Suurem:", b)
            else:
                print("Arvud on võrdsed")
            i += 1
    else:
        i = 0
        while True:
            if i >= 10:
                break
            a = float(input("Sisesta esimene arv: "))
            b = float(input("Sisesta teine arv: "))
            if a > b:
                print("Suurem:", a)
            elif b > a:
                print("Suurem:", b)
            else:
                print("Arvud on võrdsed")
            i += 1
 
 
# 11. Kahekohaliste paaritute arvude korrutis, mis jaguvad juhusliku arvuga
def ülesanne_11(t):
    jagaja = random.randint(2, 9)
    print("Juhuslik arv on:", jagaja)
    korrutis = 1
    leitud = False
 
    if t == "1":
        for arv in range(11, 100, 2):  # 11, 13, 15, ... 99
            if arv % jagaja == 0:
                korrutis = korrutis * arv
                leitud = True
    elif t == "2":
        arv = 11
        while arv < 100:
            if arv % jagaja == 0:
                korrutis = korrutis * arv
                leitud = True
            arv += 2
    else:
        arv = 11
        while True:
            if arv >= 100:
                break
            if arv % jagaja == 0:
                korrutis = korrutis * arv
                leitud = True
            arv += 2
 
    if leitud:
        print("Korrutis:", korrutis)
    else:
        print("Sobivaid arve ei leitud (paarisarvuga ei jagu ükski paaritu arv)")
 
 


while True:
    print()
    print("Vali ülesanne (7-12), 0 = välju")
    ül = input("Ülesanne: ")
 
    if ül == "0":
        print("Väljun programmist.")
        break
 
    if ül not in ("7", "8", "9", "10", "11", "12"):
        print("Vale valik, proovi uuesti.")
        continue
 
    print("Vali tsükkel: 1 = for, 2 = while, 3 = while True")
    tsukkel = input("Tsükkel: ")
 
    if tsukkel not in ("1", "2", "3"):
        print("Vale tsükkel, proovi uuesti.")
        continue
 
    if ül == "7":
        ülesanne_7(tsukkel)
    elif ül == "8":
        ülesanne_8(tsukkel)
    elif ül == "9":
        ülesanne_9(tsukkel)
    elif ül == "10":
        ülesanne_10(tsukkel)
    elif ül == "11":
        ülesanne_11(tsukkel)
    