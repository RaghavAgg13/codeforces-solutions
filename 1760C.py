''' Slow version 2 - Attempt 1 '''
# for i in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))

#     for i in range(n):
#         print(a[i]-max(a[:i]+a[i+1:]), end=' ')
#     print()

''' Slow version 1 - Attempt 2 '''
# for i in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
#     soln = []

#     m = max(a)
#     for b in a:
#         if b != m:
#             soln.append(str(b-m))
#         else:
#             l1 = list(sorted(a))
#             soln.append(str(m-l1[-2]))
            
#     print(' '.join(soln))

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    m = max(a)
    m_ = list(sorted(a))[-2]

    for b in a:
        if b != m:
            print((b-m), end=' ')
        else:
            print((m-m_), end=' ')
    print()