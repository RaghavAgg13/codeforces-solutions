a = input()
cnt = 0
cur = 0

for char in a:
    if char == '(':
        cur += 1
    elif char == ')' and cur > 0:
        # We found a matching pair
        cur -= 1
        cnt += 2

print(cnt)