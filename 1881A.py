for i in range(int(input())):
    n,m = list(map(int, input().split()))
    x = input()
    s = input()

    def length(l):
        return len(list(set(list(l))))
            

    count = 0
    while s not in x and count <= 6:
        x *= 2
        count += 1

    print(count if count != 7 else '-1')
