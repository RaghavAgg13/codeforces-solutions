for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ones = a.count(1)
    neg_ones = a.count(-1)
    count = neg_ones-ones

    operations = 0
    if count > 0:
        operations += count//2+count%2
        neg_ones -= count//2+count%2

    if neg_ones % 2 == 1: operations += 1

    print(operations)
