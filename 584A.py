n, t = list(map(int, input().split()))

smallest = int('1'+'0'*(n-1))
if smallest%t == 0: no = smallest
else: no = (smallest//t+1)*t

if int(str(no)[0]) != 0 and len(str(no)) == n: print(no)
else: print('-1')