a,b,c = sorted(list(map(int, input().split())))

if c-a >= 10: print('check again')
else: print('final', b)