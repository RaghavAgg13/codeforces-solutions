n = int(input())

for i in range(n):
    num = input()
    count = 0
    length = len(num)

    for i in  num:
        if i != '0':
            count += 1
    print(count)

    for i in range(length):
        if num[i] != '0':
            print(num[i],'0'*(length - i -1), sep='', end = ' ')
    print()