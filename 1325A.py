from math import gcd
for i in range(int(input())):
    x = int(input())

    # soln = []
    # for i in range(1, x+1):
    #     for j in range(i, x+1):
    #         val = gcd(i,j) + (i*j)//gcd(i,j)
    #         if val == x and val not in soln:
    #             soln.append([i,j])
    #             break

    # print(soln[0][0], soln[0][1])
    print(1, x-1)