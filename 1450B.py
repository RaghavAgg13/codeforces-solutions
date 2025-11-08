for i in range(int(input())):
    n,k = list(map(int, input().split()))

    distances = []
    for i in range(n):
        a,b = list(map(int, input().split()))
        distances.append([a,b])
    
    check = False
    for i in range(n):
        ok = True
        for j in range(n):
            distance = abs(distances[i][0]-distances[j][0])+abs(distances[i][1]-distances[j][1])

            if distance > k:
                ok = False
                break


        if ok: 
            check = True
            break

    print(1 if check else -1)