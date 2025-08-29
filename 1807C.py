for i in range(int(input())):
    n = int(input())
    s = input()

    a = []
    nota = []
    check = False
    for i in range(n):
        if i%2 == 0:
            if s[i] not in a: a.append(s[i])
        else:
            if s[i] not in nota: nota.append(s[i])

    for letter in a:
        if letter in nota:
            check = True
            break

    print('NO' if check else 'YES')