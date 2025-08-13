for i in range(int(input())):
    a,b,c = list(map(int, input().split()))
    m = max(a,b,c)

    if a==b==c:
        print("1 1 1")
    elif a==b==m:
        print(f"1 1 {m-c+1}")
    elif b==c==m:
        print(f"{m-a+1} 1 1")
    elif a==c==m:
        print(f"1 {m-b+1} 1")
    elif a == m:
        print(f"0 {a-b+1} {a-c+1}")
    elif b == m:
        print(f"{b-a+1} 0 {b-c+1}")
    else:
        print(f"{c-a+1} {c-b+1} 0")