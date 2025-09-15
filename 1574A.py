for i in range(int(input())):
    n = int(input())
    for j in range(n):
        print("("*j, end='')
        print("()"*(n-j), end='')
        print(")"*j)