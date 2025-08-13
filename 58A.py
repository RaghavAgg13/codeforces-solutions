a = input()
word = []
b = False
for i in range(len(a)):
    word.append(a[i])

if 'h' in word:
    word = word[word.index('h')+1:]
    if 'e' in word:
        word = word[word.index('e')+1:]
        if 'l' in word:
            word = word[word.index('l')+1:]
            if 'l' in word:
                word = word[word.index('l')+1:]
                if 'o' in word:
                    b = True

if b == True: print('YES')
else: print('NO')