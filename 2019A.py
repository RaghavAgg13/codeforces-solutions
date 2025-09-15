for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))


    if n == 1:
        print(a[0]+1)
        continue


    odd = a[::2]
    even = a[1::2]

    print(max(max(odd)+len(odd), max(even)+len(even)))