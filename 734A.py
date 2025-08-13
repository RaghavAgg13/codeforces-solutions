n = int(input())
s = input()
count_a, count_d = 0,0
for i in range(n):
    if s[i] == 'A':
        count_a += 1
    elif s[i] == 'D':
        count_d += 1

if count_a> count_d:
    print('Anton')
elif count_a < count_d:
    print('Danik')
else:
    print('Friendship')