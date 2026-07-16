from math import ceil, log2
from sys import stdin
input = stdin.readline

def get_cost(no):
    if no == 0: return 0
    return no.bit_length() + no.bit_count() - 1

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ans = float('inf')

    for V in range(18):
        moves = 0

        for i in range(n):
            tar, add = 1<<V, 1<<V
            if tar < a[i]: tar += ceil((a[i]-tar)/add)*add
            
            c_min = float('inf')
            curr = tar
            
            while curr - tar <= 60:
                c_min = min(c_min, (curr - a[i]) + get_cost(curr))
                curr += add

            moves += c_min
    
        moves -= (n-1)*V
        ans = min(ans, moves)

    print(ans)
