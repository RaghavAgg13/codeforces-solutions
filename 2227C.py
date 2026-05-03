for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    b = [i for i in a if i%6 == 0]
    b.extend([i for i in a if i%2 == 0 and i%6 != 0])
    b.extend([i for i in a if i%2 != 0 and i%3 != 0])
    b.extend([i for i in a if i%3 == 0 and i%6 != 0])

    print(*b)