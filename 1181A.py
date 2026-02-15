x,y,z = list(map(int, input().split()))
coco = x//z + y//z
x %= z
y %= z

if x+y >= z:
    print(coco+1, min(abs(z-x), abs(z-y)))
else:
    print(coco, 0)