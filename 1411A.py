for i in range(int(input())):
    n = int(input())
    a = input()

    count = 0
    for i in a[::-1]:
        if i == ')': count += 1
        else: break

    print('YES' if 2*count > n else 'NO')