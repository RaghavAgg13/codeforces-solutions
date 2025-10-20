for i in range(int(input())):
    a,b = list(map(int, input().split()))
    deposit = 0

    if (a >= b): deposit = a
    elif ((b-a*2) < 0): deposit = a-(b-a)

    print(deposit)