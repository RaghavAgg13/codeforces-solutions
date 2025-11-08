vowels = ['a', 'e', 'i', 'o', 'u']
for i in range(1):
    a = input()
    b = input()

    if len(a) != len(b): 
        print('NO')
        continue


    check = True
    n = len(a)
    for i in range(n):
        if a[i] in vowels and b[i] not in vowels:
            check = False
            break
        elif a[i] not in vowels and b[i] in vowels:
            check = False
            break

    print('YES' if check else 'NO') 