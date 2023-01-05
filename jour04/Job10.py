def chiffres():
    produit = 1
    i = 0
    L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
    while i < len(L):
        if L[i] >=25 and L[i] <=90:
            produit *= L[i]
            i+=1
        else:
            i+=1
    return(produit)

print(chiffres())