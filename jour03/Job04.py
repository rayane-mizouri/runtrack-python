def Job4():
    i = 0
    while i < 101:
        if i % 3 == 0:
            if i % 5 == 0:
                print(f"FizzBuzz")
            else:
                print(f"Fizz")
        elif i % 5 == 0:
            if i % 3 == 0:
                print(f"FizzBuzz")
            else:
                print(f"Buzz")
        else:
            print(str(i))
        i = i + 1


Job4()