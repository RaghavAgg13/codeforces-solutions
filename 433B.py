n = int(input())
prices = list(map(int, input().split()))
sort = sorted(prices)

sum_p = [0]
sum_s = [0]

for i in range(1, n+1):
    sum_p.append(sum_p[i-1]+prices[i-1])
    sum_s.append(sum_s[i-1]+sort[i-1])

for i in range(int(input())):
    t, l, r = list(map(int, input().split()))

    if t == 1:
        print(sum_p[r]-sum_p[l-1])
    elif t == 2:
        print(sum_s[r]-sum_s[l-1])
