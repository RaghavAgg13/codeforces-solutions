for i in range(int(input())):
    n = int(input())

    if n%7 == 0:
        print(n)
    else:
        a = str(n)
        for i in range(10):
            no = int(a[:len(a)-1] + str(i))

            if no%7 == 0:
                print(no)
                break
        