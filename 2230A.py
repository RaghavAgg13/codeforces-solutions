for _ in range(int(input())):
    n,a,b = list(map(int, input().split()))

    grp = n//3
    score = min(a*3, b)*grp
    score += min(a*(n%3), b)

    print(score)