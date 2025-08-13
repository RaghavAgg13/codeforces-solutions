# from collections import Counter

# def solve():
#     n = int(input())
#     l = list(map(int, input().split()))

#     counts = Counter(l)
#     soln = -1

#     for key, val in counts.items():
#         if val >= 3:
#             soln = key
#             break

#     print(soln)

# for i in range(int(input())): solve()


for i in range(int(input())): 
    n = int(input())
    l = sorted(list(map(int, input().split())))

    count = 1
    result = -1

    for i in range(n-1):
        if count == 3:
            result = l[i-1]
            break

        if l[i] == l[i+1]: 
            count += 1
        else: 
            count = 1
    if count == 3:
        result = l[i-1] 
        
    print(result)