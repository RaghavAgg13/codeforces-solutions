for i in range(int(input())):
    n,a,b = list(map(int, input().split()))
    print('NO' if abs(a-b)%2 else 'YES')