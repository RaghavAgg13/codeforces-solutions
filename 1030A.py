n = int(input())
soln = list(map(int, input().split(' ')))
b = False
for i in range(n):
    if soln[i] == 1:
        b = True

if b == True: print('HARD')
else: print("EASY")