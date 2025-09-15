from math import ceil
for i in range(int(input())):
    l,r = list(map(int, input().split()))

    # soln = 0
    # x,y=0,0
    # for a in range(l, r+1):
    #     for b in range(l, a+1):
    #         if a%b > soln:
    #             soln = a%b
    #             x=a 
    #             y=b
    # print(soln, x, y)


    if 2*l > r: print(r%l)
    else: print((r-1)//2)