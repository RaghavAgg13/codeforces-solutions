n = input()
min = int(n[1:])

n1 = n[:-1]
n2 = n[:-2]+n[-1]

if int(n) >= 0: print(n)
else: print(max(int(n1), int(n2)))