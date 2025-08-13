for i in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    evenCount = oddCount = 0
    for i in s:
        if i%2 == 0: evenCount += 1
        else: oddCount += 1

    if oddCount == evenCount or (abs(oddCount-evenCount)//2) == 0:
        print('Yes')
    else: print('No')