n = int(input())
l_1 =  list(map(int, input().split(' ')))
l_2 = sorted(l_1, reverse=False)
soln = ''

for i in l_2:
    soln += str(i) + ' '
print(soln[:-1])