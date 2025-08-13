hs = list(map(int, input().split(' ')))
print(len(hs)-len(list(dict.fromkeys(hs))))