n = int(input())
cards = list(map(int, input().split(' ')))
s, d = 0, 0

for i in range(n // 2):
    a = max(cards[0], cards[-1])
    s += a
    cards.remove(a)
    a = max(cards[0], cards[-1])
    d += a
    cards.remove(a)

if n % 2 == 1:
    s += cards[0]

print(s,d)