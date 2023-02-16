n = int(input())
a = 0
for i in range(2, n+1, 2):
    print(i, end=" ")
    a += 1
    if a == 5:
        a = 0
        print()

