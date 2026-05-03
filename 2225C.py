for i in range(int(input())):
    n = int(input())
    a = input()
    b = input()

    cnt = 0
    it = iter(range(n))
    
    for i in it:
        if a[i] == b[i]: continue

        if (i == n-1):
            cnt += 1
            continue

        c = (a[i] == a[i+1]) + (b[i] == b[i+1]) 
        if c == 2:
            next(it, None)
        elif c == 1:
            next(it, None)
            cnt += 1
        else:
            cnt += 1

    print(cnt)


# replaced with cleaner code
# for i in range(int(input())):
#     n = int(input())
#     a = input()
#     b = input()

#     cnt = 0
#     i = 0
#     while i < n:
#         if a[i] != b[i]:
#             if (i == n-1):
#                 cnt += 1
#             else:
#                 c = (a[i] == a[i+1]) + (b[i] == b[i+1]) 
#                 if c == 2:
#                     i += 1
#                 elif c == 1:
#                     i += 1
#                     cnt += 1
#                 else:
#                     cnt += 1

#         i += 1

#     print(cnt)