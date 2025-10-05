for j in range(int(input())):
    n = int(input())
    weight,endurance = list(map(int, input().split()))

    for i in range(n-1):
        w,e = list(map(int, input().split()))

        if weight <= w and endurance <= e:
            weight = -1

    print(weight)