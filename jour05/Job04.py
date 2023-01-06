message = input()
def cryptage(mot="", clé=0):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    crypté = ""

    for l in mot.lower():
        pos = alphabet.find(l)

        if pos != -1:
            crypté += alphabet[(pos + clé) % len(alphabet)]
        else:
            crypté += l
    return crypté

crypté = cryptage(message, 3)
print(message, "message codé-------->", crypté)