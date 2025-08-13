for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    
    a = []
    for i in range(n):
        if i%2 == 0: a.append(str(l[i//2]))
        else: a.append(str(l[-i//2]))

    print(' '.join(a))