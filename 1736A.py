for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    n1 = a.count(0)
    n2 = b.count(0)

    pos = sum([1 for i in range(n) if a[i] != b[i]])

    a.sort()
    b.sort()

    pos_new = sum([1 for i in range(n) if a[i] != b[i]])
    
    if pos == pos_new: print(abs(n1-n2))
    elif pos_new == 0: print(1)
    else: print(1+abs(n1-n2))