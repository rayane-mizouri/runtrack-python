def rectangle(n, b):
    i=0
    if b <=2:
        print("|", end="")
        print(n * "-", end="")
        print("|")
        print("|", end="")
        print(n * "-", end="")
        print("|")
    elif b >2:
        print("|", end="")
        print(n * "-", end="")
        print("|")

        while i < (b -2):
            print("|", end="")
            print(n * " ", end="")
            print("|")
            i+=1

        print("|", end="")
        print(n * "-", end="")
        print("|")
    print("")

rectangle(8, 3)