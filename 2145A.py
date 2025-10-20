for i in range(int(input())):
    n = int(input())

    if not n%3: print(0)
    else: print(3-n%3)