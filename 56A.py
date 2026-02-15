alcohol = ['ABSINTH', 'BEER', 'BRANDY', 'CHAMPAGNE', 'GIN', 'RUM', 'SAKE', 'TEQUILA', 'VODKA', 'WHISKEY', 'WINE']

cnt = 0
for i in range(int(input())):
    a = input()

    try:
        a = int(a)
        if a < 18: cnt += 1
    except ValueError:
        if a in alcohol: cnt += 1
    
print(cnt)