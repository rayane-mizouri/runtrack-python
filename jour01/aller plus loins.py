def e() :
    mot = input("entrez un mot ")
    special_characters = "e"
    if any(c in special_characters for c in mot):
        print("il y a un 'e' ")
    else:
        print("il n'y a pas de 'e'")
    e()

e()