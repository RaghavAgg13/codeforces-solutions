def work(a, n1, n2):
    for i in range(len(a)-1):
        if a[i] == 'a' and a[i+1] == 'b': n1 += 1
        elif a[i] == 'b' and a[i+1] == 'a': n2 +=1 
        
    for i in range(len(a)-1):
        if n1 > n2:
            if a[i] == 'a' and a[i+1] == 'b': 
                a[i] = 'b'
                n1 -= 1
        elif n1 < n2:
            if a[i] == 'b' and a[i+1] == 'a':
                a[i] == 'a'
                n2 -= 1 
        else: break

    print(n1,n2)
    return n1,n2

for i in range(int(input())):
    a = list(input())

    n1,n2 = 0,0
    n1,n2 = work(a, n1, n2)
    print(n1,n2)
    while n1 != n2:
        print(n1,n2)
        n1,n2 = work(a, n1, n2)

    print(*a, sep='')