import math
for i in range(int(input())):
    n = int(input())
    squares = sum(list(map(int, input().split())))
    if int(math.sqrt(squares)) == (math.sqrt(squares)): 
        print('YES')
    else: print('NO')