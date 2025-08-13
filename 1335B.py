al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(int(input())):
    n,a,b = list(map(int, input().split()))

    if b == a:
        if n >= 26: 
            for i in range(n//26): print(''.join(al), end='')
        print(''.join(al[:n%26]))
    elif n == a:
        print(''.join(al[:b-1]), al[b-1]*(n-b+1), end='', sep='')
        print()
    else:
        beta = al[:b-1]
        beta += al[b-1]*(a-b+1)
        soln = beta*(n//a)+beta[:n%a]

        print(''.join(soln))
