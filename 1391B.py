for i in range(int(input())):
    n,m = list(map(int, input().split()))
    
    count = 0
    for i in range(n-1):
        a = input()
        if a[-1] == 'R': count += 1

    a = input()
    count += a.count('D')
    print(count)