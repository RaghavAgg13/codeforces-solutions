def factors(x):
    arr = set()
    for i in range(2, int(x**.5)+1):
        if x%i == 0:
            arr.add(i)
            while (x%i == 0): x //= i

    
    if x != 1: arr.add(x)
    if not arr: arr.add(1)
    return sorted(list(arr), reverse=True)

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if a == sorted(a):
        print("Bob")
        continue

    f = [[] for _ in range(n)]
    for i in range(n):
        f[i] = factors(a[i])
    
    a = []
    for i in f:
        a.extend(i)

    # print(a)

    if a == sorted(a):
        print("Bob")
    else:
        print("Alice")