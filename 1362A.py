from math import log2
for i in range(int(input())):
    a,b = list(map(int, input().split()))

    if a > b: a,b = b,a

    # ratio = log2(b/a)

    if b%a:
        print(-1)
        continue 

    ratio = b//a

    pow2 = ratio>0 and ratio&(ratio-1) == 0

    if pow2:
        ratio = ratio.bit_length()-1

        moves = 0
        moves += ratio//3
        ratio %= 3
        moves += ratio//2
        ratio %= 2
        moves += ratio

            
        print(int(moves))
    else:
        print(-1)