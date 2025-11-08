from sys import stdout
print = stdout.write
 
ser = ['a', 'b', 'c']
 
for i in range(int(input())):
    a = input()
    n = len(a)
 
    check = False
    for i in ser:
        if i*2 in a:
            print("-1\n")
            check = True
            break
    if check: continue
 
    if a == "?": 
        print("a\n")
        continue
 
    if a == '??':
        print("ab\n")
        continue
 
    while ('??' in a and ('a' in a or 'b' in a or 'c' in a)) or "???" in a:
        while 'a??' in a: a = a.replace('a??', "ab?")
        while 'b??' in a: a = a.replace('b??', "ba?")
        while 'c??' in a: a = a.replace('c??', "ca?")
        while '??a' in a: a = a.replace('??a', "?ba")
        while '??b' in a: a = a.replace('??b', "?ab")
        while '??c' in a: a = a.replace('??c', "?ac")
        while '???' in a: a = a.replace('???', "?a?")
 
    a = list(a)
 
    if a[:2] == ["?", "a"]: a[:2] = "ba"
    if a[:2] == ["?", "b"]: a[:2] = "ab"
    if a[:2] == ["?", "c"]: a[:2] = "ac"
    if a[-2:] == ["c", "?"]: a[-2:] = "ca"
    if a[-2:] == ["b", "?"]: a[-2:] = "ba"
    if a[-2:] == ["a", "?"]: a[-2:] = "ab"
    
    for i in range(n):
        if a[i] == '?':
            if i < n-1 and a[i+1] != '?':
                for j in ser:
                    if (i != 0 and j != a[i-1]) and j != a[i+1]:
                        a[i] = j
                        break
 
    print(''.join(a)+"\n")