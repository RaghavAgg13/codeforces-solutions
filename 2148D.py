for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    even = []
    odd = []
    
    for i in a:
        if i%2: odd.append(i)
        else: even.append(i)

    count = 0
    odd.sort()

    if len(odd) == 0:
        print(0)
    else:
        count = sum(even)

        no = len(odd)
        a1 = sum(odd[no//2:no+1])
        
        print(a1+count)