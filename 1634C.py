from sys import stdout
print = stdout.write
for i in range(int(input())):
    n,k = list(map(int, input().split()))

    if k == 1:
        print('YES\n')
        # print(*[i for i in range(1, n+1)], sep='\n')
        print(''.join([str(i)+'\n' for i in range(1, n+1)]))
    elif not n%2:
        print('YES\n')
        for i in range(n//2):
            # print(*[2*i-1 for i in range(1+i*k, k+i*k+1)])
            # print(*[2*i for i in range(1+i*k, k+i*k+1)])
            
            print(' '.join([str(2*i-1) for i in range(1+i*k, k+i*k+1)])+"\n")
            print(' '.join([str(2*i) for i in range(1+i*k, k+i*k+1)])+"\n")
    else:
        print('NO\n')