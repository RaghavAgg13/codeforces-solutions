for i in range(int(input())):
    n = int(input())

    for i in range(10, n+1):
        check = 1
        for j in range(2, i):
            if not i%j: 
                check = 0
                break

        if check and len(list(str(i))) == len(set(list(str(i)))):
            idx = []
            for c in str(i): idx.append(str(n).index(c))
            if idx == sorted(idx):
                print(i)
                break