from math import ceil
for i in range(int(input())):
    n,k = list(map(int, input().split()))

    b = False
    if n%2==0 or n%k==0:
        b = True
    elif k%2 == 0 and n%2!=0:
        b = False
    else:
        for i in range(ceil(n/k)+1):
            if (n-k*i)%2==0:
                b = True
                break
    print('YES' if b else 'NO')