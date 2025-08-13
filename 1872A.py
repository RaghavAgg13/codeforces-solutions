for i in range(int(input())):
    a,b,c = list(map(int, input().split()))

    sum = abs(a-b)//2//c
    sum += +1 if abs(a-b)/2%c !=0 else 0
    print(sum)