t = int(input())
for i in range(t):
    count = 0
    a,b = list(map(int, input().split(' ')))
    diff = b-a
    # if abs(diff) > 10:
    #     while diff > 10:
    #         a += 10
    #         diff -=10
    #         count += 1

    #     while diff < -10:
    #         a -= 10
    #         count += 1
    #         diff += 10

    # if -10 <= diff <= 10 and diff != 0:
    #     count += 1
    # print(count)
    print(abs(diff)//10 + (1 if abs(diff) % 10 != 0 else 0))