import sys
from collections import Counter

input = sys.stdin.readline

for i in range(int(input())):
    line = input()
    n, k = map(int, line.split())

    brands = Counter()
    for i in range(k):
        a, b = map(int, input().split())
        brands[a] += b
            
    top_values = sum([value for brand_id, value in brands.most_common(n)])
    
    print(top_values)