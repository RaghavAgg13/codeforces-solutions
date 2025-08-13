for i in range(int(input())):
    n = int(input())

    twos = []
    for i in range(1, n+1): 
        twos.append(2**(n-i+1))

    sum1 = twos[0] - sum(twos[1:n//2+1]) + sum(twos[n//2+1:])
    print(sum1)