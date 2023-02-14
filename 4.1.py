N = int(input("Сколько надо цифр"))
M = int(input("Кратные чему"))
K = int(input("Больше какого числа"))
x = [i for i in range(K, N, M)]
print(x)


