for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    rem = sum(a) % 3

    if rem == 0:
        print(0)
    elif rem == 2:
        print(1)
    else:
        found_rem1 = False
        for x in a:
            if x % 3 == 1:
                found_rem1 = True
                break
        
        if found_rem1:
            print(1)
        else:
            print(2)