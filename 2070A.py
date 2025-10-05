for i in range(int(input())):
    n = int(input())

    final = n//15*3 + 1
    n %= 15

    if n >= 2: final += 2
    else: final+= n
    print(final)