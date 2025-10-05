from math import sqrt

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    check = 0   
    for i in a:
        if int(sqrt(i)) != sqrt(i):
            check = 1
            break


    print('YES' if check else 'NO')