import math
n,k = list(map(int, input().split(' ')))

max_time = 240-k
sum_of_lvls_into2 = (max_time*2) / 5 

lvls = math.floor((math.sqrt(4 * sum_of_lvls_into2 + 1) - 1)/2)

print(lvls if lvls < n else n)