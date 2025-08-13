alphabets = '-abcdefghijklmnopqrstuvwxyz'

s = input()
initialPos = 'a'
count = 0
for i in s:
    alpha = abs(alphabets.index(i) - alphabets.index(initialPos))
    steps = min(alpha, abs(26 - alpha))
    count += steps
    initialPos = i

print(count)