for i in range(int(input())):
    n = int(input())

    if n >= 30+1:
        print('YES')
        if n-30 not in [6,10,14]: print(f"6 10 14 {n-30}")
        else: print(f"6 10 15 {n-31}")
    else: print('NO')
    