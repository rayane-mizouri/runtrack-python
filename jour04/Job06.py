import random
L = [random.randint(0,10) for i in range(5)]
print(L)
L[0], L[4] = L[4], L[0]
print(L)