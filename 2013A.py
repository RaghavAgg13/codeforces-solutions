for i in range(int(input())):
    n = int(input())
    a,b = list(map(int, input().split()))
    if a <= b: print(n//a+bool(n%a))
    else: print(n//b+bool(n%b))