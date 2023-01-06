def luke(note):
    if note<40:
        print("Vous avez échoué au test")
    elif note>=40:
        if note % 5 >= 3 or note % 5 == 0:
            arrondi = note
            while arrondi % 5 != 0:
                arrondi+=1
            print(arrondi,"bien joué")
        else:
            arrondi = note
            print(arrondi)

luke(10)
luke(40)
luke(83)
