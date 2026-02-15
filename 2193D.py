for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())), reverse=True)
    b = list(map(int, input().split()))

    score = 0
    sum = 0
    for i in range(n):
        sum += b[i]
        if sum > n: break

        strength = a[sum-1]

        score = max(score, (i+1)*strength)

        # print('iter', sum, strength, i, score)

    print(score)