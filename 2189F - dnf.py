for i in range(int(input())):
    n = int(input())
    a = input()

    ones = a.count('1')

    if (ones == 0):
        print(-1)
        continue

    if ones >= (n+1)//2:
        print(n)
    else:
        freq = []
        ones, zeros = 0,0

        for i in a:
            if i == '1': ones += 1
            else: zeros += 1

            freq.append([ones, zeros])

        
        