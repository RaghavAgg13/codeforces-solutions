for i in range(int(input())):
    s = input()
    t = input()

    count = 0
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            count += 1
        else:
            break

    f1 = len(s)+len(t)
    f2 = f1-count+1
    print(min(f1,f2))