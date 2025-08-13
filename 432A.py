n, k = list(map(int, input().split(' ')))
yi = sorted(list(map(int, input().split(' '))))

no_of_grps = (n - yi.count(5)) // 3
count = 0

for i in range(no_of_grps):
    s = yi[i*3:i*3+3]
    if 5-s[-1] >= k:
        count += 1
print(count)