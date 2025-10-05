for i in range(int(input())):
    a,b,c = list(map(int, input().split()))


    sum = a+b+c
    if sum%3: 
        print('NO')
    else:
        avg = sum//3
        if avg >= a and avg >= b and c >= avg:
            print('YES')
        else:
            print('NO')