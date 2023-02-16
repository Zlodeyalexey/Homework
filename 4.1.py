N = int(input("Сколько надо цифр"))
M = int(input("Кратные чему"))
K = int(input("Больше какого числа"))

while N:
    if K % M == 0:
        N -= 1
        print(K, end=" ")
        K += M
    else:
        K += 1


