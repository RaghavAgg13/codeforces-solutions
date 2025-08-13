n = int(input())
scores = list(map(int, input().split(' ')))
count = 0

for i in range(1,n):
    b = False
    if scores[i] > scores[i-1]:
        b = True
        for score in scores[:i-1]:
            if scores[i] > score:
                b = True
            else: 
                b = False
                break

    if scores[i] < scores[i-1]:
        b = True
        for score in scores[:i-1]:
            if scores[i] < score:
                b = True
            else: 
                b = False
                break
    if b == True: count += 1
print(count)