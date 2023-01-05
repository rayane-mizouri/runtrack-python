#suite = [22.4, 4.0,16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
#suite.sort()
#print(suite)

a = int(22.4*1)
a = (float(a))/1

b = int(4.0*1)
b = (float(b))/1

c = int(16.22*1)
c = (float(c))/1

d = int(9.10*1)
d = (float(d))/1

e = int(11.0*1)
e = (float(e))/1

f = int(12.22*1)
f = (float(f))/1

g = int(14.20*1)
g = (float(g))/1

h = int(5.20*1)
h = (float(h))/1

i = int(17.50*1)
i = (float(i))/1

alphabet = a,b,c,d,e,f,g,h,i
beta = [a,b,c,d,e,f,g,h,i]

def trier(beta):
    r = []
    while beta:
        mini = min(beta)
        beta.remove(mini)
        r.append(mini)
    return r
print(trier(beta))