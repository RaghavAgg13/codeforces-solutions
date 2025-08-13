l1 = list(map(str, input()[1:-1].split(", ")))
if l1 != ['']:
    print(len(dict.fromkeys(l1)))
else:
    print('0')