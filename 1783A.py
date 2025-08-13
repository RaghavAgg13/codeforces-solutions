for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    s = [max(a)]
    a.remove(s[0])
    sum = s[0]
    for i in range(n):
        for i in a:
            if i != sum:
                sum += i
                s.append(i)
                a.remove(i)
 
    if len(s) == n:
        print("YES")
        print(*s)
    else:
        print('NO')