for i in range(int(input())):
    a,b = list(map(int, input().split()))
    if a == b: print(0)
    elif not a%b or not b%a: print(1)
    else: print(2)