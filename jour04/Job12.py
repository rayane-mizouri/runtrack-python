list = [786, 65, 98, 4, 8, 5, 43]

beta = list

def trier(beta):
    r = []
    while beta:
        mini = min(beta)
        beta.remove(mini)
        r.append(mini)
    return r
print(trier(beta))