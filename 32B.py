s = input()
j = 0

while j <= len(s)-1:
    if s[j] == '-':
        if s[j+1] == '-':
            print('2', end = '')
        else:
            print('1', end = '')
        j += 2
    else:
        print('0', end = '')
        j += 1