print("Veuillez mettre des nombres comme dans l'example:1,1,1")
a, b, c = eval(input())
if a < (b + c) and b < (a + c) and c < (a + b):
    print("Ces trois longueurs déterminent bien un triangle.")
else:
    print("valeur erronée")
    exit()

f = 0
if a == b and b == c:
    print("c'est triangle équilatéral.")
    f = 1
elif a == b or b == c or c == a:
    print("c'est triangle isocèle.")
    f = 1
if a * a + b * b == c * c or b * b + c * c == a * a or c * c + a * a == b * b:
    print("c'est un triangle rectangle.")
    f = 1
if f == 0:
    print("c'est un triangle quelconque.")