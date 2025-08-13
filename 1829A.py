check = 'codeforces'
t = int(input())

for i in range(t):
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] != check[i]:
            count += 1
    print(count)