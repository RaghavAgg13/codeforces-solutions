for i in range(int(input())):
    a = input()
    text = input()

    sum = 0
    for i in range(1, len(text)):
        letter = text[i]
        sum += abs(a.index(text[i])-a.index(text[i-1]))

    print(sum)