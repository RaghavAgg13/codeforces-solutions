for i in range(int(input())):
    n = int(input())
    a = input()

    count = [0]*4
    for i in a:
        if i == 'A': 
            if count[0] < n: count[0] += 1
        elif i == 'B': 
            if count[1] < n: count[1] += 1
        elif i == 'C': 
            if count[2] < n: count[2] += 1
        elif i == 'D': 
            if count[3] < n: count[3] += 1

    print(sum(count))