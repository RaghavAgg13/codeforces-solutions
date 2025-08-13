#slow as shit but works
# for i in range(int(input())):
#     n,k = list(map(int, input().split()))
#     a = list(input())
#     count = 0


#     while 'B' in a:
#         if 'B' in a: start = a.index('B')

#         a[start:start+k] = ['W']*k
#         count += 1

#     print(count)

#how tf did this work?????
for i in range(int(input())):
    n,k = list(map(int, input().split()))
    a = list(input())
    bs = []

    for i in range(n):
        if a[i] == 'B': bs.append(i)

    if bs != []:
        count = 1
        start = bs[0]
        for i in bs[1:]:
            if i - start > k-1:
                count += 1
                start = i

        print(count)
    else: print(0)