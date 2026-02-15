for i in range(int(input())):
    n,a = list(map(int, input().split()))
    no = list(map(int, input().split()))

    less, greater = 0,0
    for i in range(n):
        if no[i] < a: less += 1
        elif no[i] > a: greater += 1
    
    if greater >= less: print(a+1)
    elif greater < less: print(a-1)