for i in range(int(input())):
    n = int(input())
    l = list(sorted(list(map(int, input().split()))))

    sum = 0
    for i in l:
        if i < 0: sum -= i
        else: sum += i

    print(sum)