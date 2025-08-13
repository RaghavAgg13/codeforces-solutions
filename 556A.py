n = int(input())
l = input()

n1 = '0'*n
n2 = '1'*n

if l == n1 or l == n2:
    print(n)
else:
    # while '10' in l or '01' in l:
    #     idx = l.index('10' if '10' in l else '01')
    #     l = l[:idx]+l[idx+2:]

    # print(len(l))
    print(abs(l.count('0')-l.count('1')))