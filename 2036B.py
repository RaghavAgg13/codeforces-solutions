import sys

num_test_cases = int(sys.stdin.readline())
for _ in range(num_test_cases):
    n, k = map(int, sys.stdin.readline().split())
    brands = {} 
    
    for i in range(k):
        a, b = map(int, sys.stdin.readline().split())
        
        if a not in brands: brands[a] = b
        else: brands[a] += b
            
    print(sum(sorted(brands.values(), reverse=True)[:n]))