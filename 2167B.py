for i in range(int(input())):
    n = input()
    a,b = list(map(str, input().split()))

    print("YES" if sorted(a) == sorted(b) else 'NO')