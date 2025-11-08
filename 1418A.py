from math import log, ceil
for i in range(int(input())):
    x,y,k = list(map(int, input().split()))

    sticks = k*(y+1)-1
    moves = (sticks+x-2)//(x-1)
    ans = moves+k
    covered = 0
    while covered>sticks:
        moves = int(log(ans-covered, x))
        covered += k**moves
        ans += 2**moves
    print(ans)