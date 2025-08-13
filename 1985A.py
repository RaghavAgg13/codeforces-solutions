t = int(input())

for i in range(t):
    a,b = list(map(str, input().split()))

    if a != b:
        if a[0] != b[0]:
            print(b[0],a[1:], " ", a[0], b[1:], sep='')
        else:
            print(a,b)
    else:
        print(a,b)