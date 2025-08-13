for i in range(int(input())):
    n,s = list(map(int, input().split()))
    pos = []
    vel = []
    for i in range(n):
        val = list(map(int, input().split()))
        pos.append(val[:2])
        vel.append(val[2:])


        if len(list(set(pos))) == n:
            for i in range(n):
                pos[i][0] += vel[i][0]
                pos[i][1] += vel[i][1]
        else:
            for i in range(n):
                if pos.count(pos[i]) != 1:
                    p1 = pos[i]
                    v1 = vel[i]
                    idx1 = pos.index(p1)
                    pos.remove(p1)
                    idx2 = pos.index(p1)
                    pos.remove(p1)
                    v2 = vel[idx2]

                    v3 = v1

                    v1 = v2
                    v2 = v3

                    vel







        