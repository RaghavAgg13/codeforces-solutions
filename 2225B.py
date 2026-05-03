# for _ in range(int(input())):
#     a = input()
#     n = len(a)

#     l,r = -1,-1
#     for i in range(1, n):
#         if a[i] == a[i-1]:
#             l = i
#             break
#     for i in range(n-1, 0, -1):
#         if a[i] == a[i-1]:
#             r = i
#             break

#     if ('aa' not in a and 'bb' not in a) or l == r:
#         print("YES")
#     else:
#         d = ''
#         for le in a[l:r]:
#             if le == 'a': d += 'b'
#             else: d += 'a'
        
#         b = a[:l] + d + a[r:]
#         c = a[:l] + d[::-1] + a[r:]

#         # print(d, b, c)

#         if ('aa' not in b and 'bb' not in b) or ('aa' not in c and 'bb' not in c):
#             print("YES")
#         else:
#             print("NO")

# solution #2

for _ in range(int(input())):
    a = input()
    n = len(a)

    b = ("ba"*((n+1)//2))[:n]
    c = ("ab"*((n+1)//2))[:n]
    
    arr = [i for i in range(n) if a[i] != b[i]]
    c1 = (not arr or len(arr) == arr[-1]-arr[0]+1)

    if c1:
        print("YES")
        continue

    arr = [i for i in range(n) if a[i] != c[i]]
    c2 = (not arr or len(arr) == arr[-1]-arr[0]+1)

    if c2:
        print("YES")
    else:
        print("NO")

# final answer is of only two forms b or c here
# just check if the diff is a contiguous block or not