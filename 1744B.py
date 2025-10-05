for i in range(int(input())):
    n,q = list(map(int, input().split()))
    a = list(map(int, input().split()))

    count = 0
    sum = 0
    for i in a:
        count += i%2
        sum += i

    even,odd = 0,0

    for i in range(q):
        t,a = list(map(int, input().split()))

        if t%2:
            even, odd = 0,a
        else: 
            even, odd = a,0

        sum += odd*count+even*(n-count)
        print(sum)

        if t%2:
            if a%2: count = 0
        else: 
            if a%2: count = n