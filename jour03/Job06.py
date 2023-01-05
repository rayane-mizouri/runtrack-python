import string

alphabet=string.ascii_lowercase
alphabet= alphabet * 10

i = 1

while i <= len(alphabet):
    print(alphabet[:i])
    alphabet = alphabet[i:]

    i += 1
