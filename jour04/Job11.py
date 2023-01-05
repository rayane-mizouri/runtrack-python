L = [7, 11, 42, 39, 2]

def nombre(chiffre):
    i = 0
    while i < len(chiffre):
	    chiffre[i]+=1
	    i+=1
    return(chiffre)

print(nombre(L))
