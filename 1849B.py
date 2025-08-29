# for i in range(int(input())):
#     n,k = list(map(int, input().split()))
#     a = list(map(int, input().split()))

#     while max(a) > 0:
#         idx = a.index(max(a))
#         a[idx] -= k
#         if a[idx] <= 0:
#             print(idx+1, end=' ')
#     print()

for i in range(int(input())):
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a = [i%k for i in a]

    soln = []
    for i in range(n):
            if a[i] == 0:
                soln.append((k, i))
            else:
                 soln.append((a[i], i))
    
    soln.sort(key=lambda x: (-x[0], x[1]))
    print(*[j+1 for i,j in soln])