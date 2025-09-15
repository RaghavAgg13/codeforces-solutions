from math import ceil
for i in range(int(input())):
    n,s = list(map(int, input().split()))
    
    idx = n//2+n%2
    median = s//(n-idx+1)
    print(median)