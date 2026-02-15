m = list(map(int, input().split()))
w = list(map(int, input().split()))
h = list(map(int, input().split()))

sum = h[0]*100 - h[1]*50

for i in range(1, 6):

    sum += max(0.3*500*i, (1-m[i-1]/250)*500*i - 50*w[i-1])

print(int(sum))