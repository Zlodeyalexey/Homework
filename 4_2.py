while True:
    a = float(input("введите число: "))
    b = input("умножаем делим аль чего еще(+, -, *, /: ")
    c = float(input("вводим второе число: "))
    if b == "+":
        print(a + c)
     elif b == "*":
         print(a * c)
    elif b == "-":
        print(a - c)
    elif b == "/":
        print(a/c)
    else:
         print("Skynet error")