for i in range(int(input())):
    a = input()

    count = 0
    s = ""
    repo = ""

    if len(set(a)) == 1: count = 1
    else:
        for i in a:
            if i not in repo:
                s += i
                repo = ''

            if len(set(s)) == 3: 
                count += 1
                repo = s
                s = ''

        if s != '': count += 1
    print(count)