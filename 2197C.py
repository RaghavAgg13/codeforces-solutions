for i in range(int(input())):
    p,q = list(map(int, input().split()))


    if (p >= q): print("Alice")
    elif q-p >= 0 and 3*p-2*q >= 0:
        print("Bob")
    else: print("Alice") 