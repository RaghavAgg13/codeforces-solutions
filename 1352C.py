t = int(input())

for i in range(t):
    n,k = list(map(int, input().split()))

    no = k + (k - 1) // (n - 1)
    print(no)