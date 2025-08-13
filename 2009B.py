for i in range(int(input())):
    n = int(input())
    s = []
    for i in range(n):
        word = input()
        for i in word:
            if i == '#': idx = str(word.index(i)+1)
        s.append(idx)

    s = list(reversed(s))

    print(' '.join(s))