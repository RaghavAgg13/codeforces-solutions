for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    count = 0
    repo = []
    for i in range(n-1):
        for j in range(i+1, n):
            diff = abs(a[i]-a[j])
            if abs(diff) not in repo:
                repo.append(diff)
                count += 1

    print(count)