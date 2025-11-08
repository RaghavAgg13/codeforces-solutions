b = input()
a = input()

n1 = ord(a[0])-ord(b[0])
n2 = int(a[1])-int(b[1])

moves = max(abs(n1), abs(n2))
print(moves)

s1 = (n1 > 0) * "R" + (n1 < 0) * "L"
s2 = (n2 > 0) * "U" + (n2 < 0) * "D"

common = min(abs(n1), abs(n2))

print(f"{s1+s2}\n" * common, end="")
print(f"{s1 if abs(n1) > abs(n2) else s2}\n" * (moves-common), end="")