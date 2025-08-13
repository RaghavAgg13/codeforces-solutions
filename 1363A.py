for i in range(int(input())):
    n,x = list(map(int, input().split()))
    a = list(map(int, input().split()))

    b = False
    evenCount = sum(1 for i in a if i%2==0)
    oddCount = n-evenCount

    for odd_count in range(1, min(oddCount, x) + 1, 2):
        even_count = x - odd_count
        if even_count <= evenCount:
            b = True
            break

    print('YES' if b else 'NO')