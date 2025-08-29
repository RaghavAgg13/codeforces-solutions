for i in range(int(input())):
    n = int(input())
    ini = input()
    fin = input()

    count1to0, count0to1 = 0,0

    for i in range(n):
        a = ini[i]
        b = fin[i]
        if a == '1' and b == '0': count1to0+=1
        elif a == '0' and b == '1': count0to1+=1

        print(max(count1to0, count0to1))