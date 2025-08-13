s = list(map(int, input().split("+")))
word = ''
s.sort()
for i in s:
    word += str(i) + '+'
print(word[:-1])
