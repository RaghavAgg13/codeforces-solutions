k,r = list(map(int, input().split(' ')))

for i in range(1, 10):
    if (k * (i) - r) % 10 == 0 or (k*i % 10 == 0 and i < 10):
        print(i)
        break