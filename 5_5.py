numbers = [23, 7, 30, 38, 34, 4, 2, 200]
for i in range(len(numbers) // 2):
    numbers[i], numbers[~i] = numbers[~i], numbers[i]

print(numbers)



