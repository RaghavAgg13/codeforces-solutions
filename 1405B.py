for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split())) + [0]

    cnt = 0
    cur_sum = 0
    for i in range(n):
        if a[i] > 0:
            a[i+1] += a[i]
    
    print(a[-1])