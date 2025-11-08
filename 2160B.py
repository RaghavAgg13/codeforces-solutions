from sys import stdin, stdout
input = stdin.readline
print = stdout.write
 
for i in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
 
    a = ["1"]
    cur = 1
    for i in range(1, n):
        if b[i] == b[i-1]+i+1:
            cur += 1
            a.append(str(cur))
        else:
            a.append(str(a[i-b[i]+b[i-1]]))
    
    print(' '.join(a))
    print("\n")
