n = int(input())
cmds = list(map(int, input().split(' ')))
police, crimes = 0,0

for cmd in cmds:
    if cmd >= 1:
        police += cmd
    elif cmd == -1:
        if police == 0:
            crimes += 1
        else:
            police -= 1
print(crimes)