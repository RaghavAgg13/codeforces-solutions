n, k, l, c, d, p, nl, np = list(map(int, input().split(' ')))

total_drink = k * l
total_drink_req = n * nl
n1 = total_drink / total_drink_req

total_salt = p
total_salt_req = n * np
n2 = total_salt / total_salt_req

nos = int(min(n1, n2, (c*d)/n, (p / np) / n))
print(nos)