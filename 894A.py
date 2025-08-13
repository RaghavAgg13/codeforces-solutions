s = input()
n = len(s)

count = 0
for i in range(n-2):
    if s[i] == 'Q':
        for j in range(i+1, n-1):
            if s[j] == 'A':
                count += s[j+1:].count('Q')


print(count)