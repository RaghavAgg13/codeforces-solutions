for i in range(int(input())):
    n, x = list(map(int, input().split()))
    s = list(map(int, input().split()))
    
    fuels = [(x-s[-1])*2, s[0]]
    for i in range(1, n):
        fuels.append(s[i]-s[i-1])
    print(max(fuels))