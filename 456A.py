n = int(input())
laptops = []

for i in range(n):
    a, b = map(int, input().split())
    laptops.append((a, b))

# Sort laptops by price
laptops.sort()

for i in range(n - 1):
    if laptops[i][1] > laptops[i + 1][1]:
        print("Happy Alex")
        break
else:
    print("Poor Alex")