import math
n = int(input())
a = input()

alp = int((-1+math.sqrt(1+8*n))//2)
for i in range(alp):
    print(a[i*(i-1)//2 +  i], end='')

