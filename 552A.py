sum = 0
for i in range(int(input())):
    a,b,c,d = list(map(int, input().split()))

    sum += (c-a+1)*(d-b+1)

print(sum)