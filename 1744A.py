for i in range(int(input())):
    n = int(input())
    w = list(map(int, input().split()))
    a = input()

    check = True
    for i in set(w):
        indices = [index for index, element in enumerate(w) if element == i]
        if len(indices) > 1:
            for indice in indices[1:]:
                if a[indices[0]] != a[indice]:
                    check = False
                    break
        if not check: break

    print('YES' if check else 'NO')