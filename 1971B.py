from random import shuffle
def shuffle_word(word):
    word = list(word)
    shuffle(word)
    return ''.join(word)

for i in range(int(input())):
    s = input()


    if len(set(s)) == 1:
        print('NO')
    elif len(s) == 2:
        print('YES')
        print(s[::-1])
    else:
        print('YES')
        w = shuffle_word(s)
        while w == s: w = shuffle_word(s)
        print(w)