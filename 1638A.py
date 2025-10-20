for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    idx = 0
    no = 1
    check = True
    for i in range(n):
        if check:
            if a[i] == i+1:
                no += 1
                idx += 1
            else: 
                check = False
                break

    for i in range(n):
        if a[i] == no:
            a[idx:i+1] = a[idx:i+1][::-1]
            break

    print(*a)