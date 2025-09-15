for i in range(int(input())):
    n,k = list(map(int, input().split()))

    no_of_diagonals = n*2-1
    max_length = n
    count = 0

    if k >= max_length:
        count = 1
        k -= max_length
        max_length -= 1

    while k > 0 and k > max_length*2:
        count += 2
        k -= max_length*2
        max_length -= 1

    if k > max_length: count += 2
    elif 0 < k <= max_length: count += 1
    print(count)