for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    n1,n2 = [0], [0]
    for i in range(n):
        n1.append(a[i]+n1[-1])
    for i in range(m):
        n2.append(b[i]+n2[-1])
    
    print(max(n1)+max(n2))