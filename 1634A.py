for i in range(int(input())):
    n,k = list(map(int, input().split()))
    a = input()

    if k == 0 or a == a[::-1]: print(1)
    else: print(2)