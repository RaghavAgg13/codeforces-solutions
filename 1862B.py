for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    l = [str(a[0])]
    for i in range(1, n):
        if a[i] < a[i-1]: l.append('1')
        l.append(str(a[i]))

    print(len(l))
    print(' '.join(l))



#     l = a.copy()
 
#     idx = 1
#     count = 0
#     while idx <= n-1:
#         if int(a[idx]) < int(a[idx-1]):
#             l.insert(idx + count, '1')
#             count += 1
#         idx += 1
    
#     print(len(l))
#     print(' '.join(l))