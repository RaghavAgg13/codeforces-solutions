n = int(input())
initial = list(map(int, input().split()))
final = sorted(initial)

check = [True]*n
for i in range(n):
    check[i] = initial[i] == final[i]

if check == [True]*n or list(reversed(initial)) == final or (n%2==1 and check == [False]*(n//2)+[True]+[False]*(n//2)):
    print('yes')
    print('1 1' if check == [True]*n else f'1 {n}')
else:
    # count = []
    # work = 0
    # for j in range(n):  
    #     i = check[j]

    #     if not i:
    #         work += 1
    #     else:
    #         if work != 0: count.append([j, work])
    #         work = 0
    # if work != 0 and not check[-1]: count.append([n, work])

    # print(count)

    # if len(count) == 1 or (len(count) == 2 and len):
    #     i_f = count[0][0]
    #     i_i = i_f - count[0][-1] + 1

    #     # print(list(reversed(initial[i_i-1 : i_f])))
    #     # print(final[i_i-1 : i_f])

    #     if list(reversed(initial[i_i-1 : i_f])) == final[i_i-1 : i_f]:
    #         print('yes')
    #         print(i_i, i_f)
    #     else:
    #         print('no')
    # else:
    #     print('no')

    start = check.index(False) + 1
    end = n - list(reversed(check)).index(False)
    
    if list(reversed(initial[start-1 : end])) == final[start-1 : end]:
        print('yes')
        print(start, end)
    else:
        print('no')