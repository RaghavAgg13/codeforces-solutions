def recur(upper, lower):
    if (upper == 1 and lower == 1): return 1
    b = upper//2
    d = lower//2
    upper = b + upper%2
    lower = d+lower%2+b
    return recur(upper, lower)+b+d
    

for i in range(int(input())):
    n = int(input())
    a = recur(n, 0)
    print(a)