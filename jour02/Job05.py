def calcule(num1, signe, num2):

    if signe == "+":
        resultat = num1 + num2
    elif signe == "-":
        resultat = num1 - num2
    elif signe == "*":
        resultat = num1 * num2
    elif signe == "/":
        resultat = num1 / num2
    elif signe == "%":
        resultat = num1 % num2
    return (resultat)

print(calcule(20, "+", 4))
print(calcule(18, "-", 2))
print(calcule(80, "*", 67))
print(calcule(40, "/", 8))
print(calcule(88, "%", 24))