keys = [[], [2,3,4,5], [1,3,4,6], [1,2,5,6], [1,2,5,6], [1,3,4,6], [2,3,4,5]]

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    cnt = 0
    for i in range(n-1):
        if a[i+1] not in keys[a[i]]:
            cnt += 1
            if (i+2 < n):
                for key in keys[a[i+2]]:   
                    if key in keys[a[i]]:
                        a[i+1] = key
                        break

    print(cnt)

