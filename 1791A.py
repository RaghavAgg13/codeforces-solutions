s = sorted(list(dict.fromkeys(list(map(str, 'codeforces')))))

for i in range(int(input())):
    if input() in s:
        print('YES')
    else:
        print('NO')