for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if a.count(0) >= 3 and a.count(1) >= 1 and a.count(2) >= 2 and a.count(3) >= 1 and a.count(5) >= 1:
        count = [0]*(max(a)+1)
        for j in range(n):
            i = a[j]
            count[i] += 1

            if count[0] >= 3 and count[1] >= 1 and count[2] >= 2 and count[3] >= 1 and count[5] >= 1:
                print(j+1)
                break
    else: print(0)
