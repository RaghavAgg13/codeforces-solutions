for i in range(int(input())):
    a = input()
    score = int(a[0])
    if a[0] == '0': score += 10
    for i in range(3):
        b = int(a[i])
        if b == 0: b = 10

        c = int(a[i+1])
        if c == 0: c = 10

        score += abs(b-c)+1

    print(score)
