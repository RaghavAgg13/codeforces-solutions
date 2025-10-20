for i in range(int(input())):
    n = int(input())
    a = input()

    if a == "?"*n:
        print('B'*(n%2), 'RB'*(n//2), sep='')
    else:
        while "?" in a:
            if "?B" in a: a = a.replace("?B", "RB")
            if "B?" in a: a = a.replace("B?", "BR")
            if "?R" in a: a = a.replace("?R", "BR")
            if "R?" in a: a = a.replace("R?", "RB")
        print(a)