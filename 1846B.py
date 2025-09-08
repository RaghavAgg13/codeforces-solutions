for i in range(int(input())):
    a = []
    for i in range(3): a.append(input())

    final = 'DRAW'
    if 'XXX' in a:
        final = "X"
    elif 'OOO' in a:
        final = 'O'
    elif '+++' in a:
        final = "+"
    elif a[0][0] == a[1][0] == a[2][0] != '.':
        final = a[0][0]
    elif a[0][1] == a[1][1] == a[2][1] != '.':
        final = a[0][1]
    elif a[0][2] == a[1][2] == a[2][2] != '.':
        final = a[0][2]
    elif a[0][0] == a[1][1] == a[2][2] != '.':
        final = a[0][0]
    elif a[0][2] == a[1][1] == a[2][0] !='.':
        final = a[0][2]

    print(final)