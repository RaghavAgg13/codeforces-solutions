for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    d = [a[i]-b[i+1] for i in range(n-1) if a[i]-b[i+1] > 0]
    print(sum(d)+a[-1])