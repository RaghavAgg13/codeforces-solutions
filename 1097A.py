# suit = ['D', 'C' 'S', 'H']
# rank = [2,3,4,5,6,7,8,9,'T', 'J', 'Q', 'K', 'A']

card = input()
suit = card[0]
rank = card[1]

cards = list(map(str, input().split()))
suits = []
ranks = []

for card_ in cards:
    suits.append(card_[0])
    ranks.append(card_[1])

if suit in suits or rank in ranks:
    print('YES')
else: print('NO')