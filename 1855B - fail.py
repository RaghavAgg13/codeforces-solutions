for i in range(int(input())):
    n = int(input())

    small = []
    large = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            small.append(i)
            if i != n//i: large.append(n//i)

    large.reverse()
    factors = small+large

    final = count = 1
    for i in range(len(factors)-1):
        if factors[i+1]-factors[i] == 1:
            count += 1
        else:
            final = max(final, count)
            count = 1

    print(final)