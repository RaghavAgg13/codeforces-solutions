al = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for i in range(int(input())):
    n = int(input())
    a = input()

    alpha = [0]*26

    for i in range(n):
        letter = a[i]
        alpha[al.index(letter)] += 1

    count = sum([1 for i in range(26) if alpha[i] > i])
    print(count)