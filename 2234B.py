from sys import stdin
input = stdin.readline

for i in range(int(input())):
    n = int(input())

    for a in range(0, 10):
        if n >= a and (n-a)%12 == 0:
            print(a,n-a)
            break
    else:
        found = False
        for i in range(1, min(n,3)):
            st = str(i)[::-1]
            for j in range(11):
                if j == 10:
                    a = i*(10**len(st)) + int(st)
                else:
                    a = i*(10**(len(st)+1)) + j*(10**len(st)) + int(st)

                if a <= n and (n-a)%12 == 0:
                    print(a,n-a)
                    found = True 
                    break
        
            if found: break
        
        if not found: print(-1)