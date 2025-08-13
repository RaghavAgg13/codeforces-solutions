n = int(input())
count = 1
rowElement = 1
while n >= rowElement:
    n -= rowElement
    count += 1
    rowElement = count*(count+1)/2

print(count-1)