# MASSIVE FAIL IM DUMB
# for i in range(int(input())):
#     n = int(input())
#     a = input()
#     s = [0]

#     b = False
#     for i in range(n):
#         if a[i] == '<':
#             if a[i+1:].count(">") > a[i+1:].count("<"):
#                 s.append(max(s) if max(s) > s[-1] else s[-1] + 1) 
#             # if max(s) > s[-1]:
#             #     for j in range(len(s)-1):
#             #         if s[j] > s[-1]:
#             #             s.append(s[j])
#             #             break
#             # else:
#             else: s.append(s[-1]+1)
#         else:
#             if a[i+1:].count("<") > a[i+1:].count(">"):
#                 s.append(min(s) if min(s) < s[-1] else s[-1]-1)
#             # if min(s) < s[-1]:
#             #     for j in range(len(s)-1):
#             #         if s[j] < s[-1]:
#             #             s.append(s[j])
#             #             break
#             # else:
#             else: s.append(s[-1]-1)

#     print(s)
#     print(len(set(s)))


for i in range(int(input())):
    n = int(input())
    a = input()

    final = 1
    count = 1
    for i in range(1, n):
        if a[i] == a[i-1]:
            count += 1
        else:
            final = max(final, count)
            count = 1
    final = max(final, count)
    print(final+1)