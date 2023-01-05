import random
l = [random.randint(0,10) for i in range(5)]
somme = l[2] + l[4]
print(l)
print(l[1])
del l[3]
l.insert(3, somme)
print(l)
print(l[4])
