a = []
for i in range(int(input())):
    word = input()

    if word not in a:
        print('NO')
        a.append(word)
    else:
        print('YES')