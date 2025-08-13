for i in range(int(input())):
    l = int(input())
    print(l//4 + 1 if l%4 != 0 else l//4)