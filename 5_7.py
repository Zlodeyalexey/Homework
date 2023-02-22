S = [23, 7, 30, 38, 34, 4, 2, 200]
for i in range(len(S)):
    if i == len(S) - 1:
        print(S[i-1] + S[0])
    else:
        print(S[i-1] + S[i+1])
