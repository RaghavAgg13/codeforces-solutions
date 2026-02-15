arr = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
from math import log2, ceil
n = int(input())

value = (n + 5) / 10
log_value = log2(value)
k = ceil(log_value + 1)

# print(k)
start,end = (10 * (2**(k - 2))) - 4, (10 * (2**(k - 1))) - 5
# print(start, end)

lvl = 2**(k-1)

for i in range(5):
    if start+i*lvl <= n < start+(i+1)*lvl:
        print(arr[i])
        break