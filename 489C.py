m, s = list(map(int, input().split()))

small = int('1' + '0'*(m-1))
large = int('9'*m)

def solve(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum


if s == 0:
    if m == 1: print('0 0')
    else: print('-1 -1')
else:
    if s > 9*m: print('-1 -1')
    else:
        smallest = []
        largest = []
        sum_s = sum_l = s

        for i in range(m):
            for j in range(0 if i > 0 else 1,10):
                if sum_s - j <= 9 * (m - i - 1):
                    smallest.append(str(j))
                    sum_s -= j
                    break

            d = min(9, sum_l)
            largest.append(str(d))
            sum_l -= d
        
        print(''.join(smallest), ''.join(largest))