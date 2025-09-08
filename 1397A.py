for i in range(int(input())):
    alpha = [0]*26

    n = int(input())
    for i in range(n):
        a = input()
        for i in a:
            alpha[ord(i)-97] += 1

    check = True
    for i in alpha:
        if i%n != 0:
            check = False
            break

    print('YES' if check else 'NO')