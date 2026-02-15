for i in range(int(input())):
    n,m,k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    cmds = input()

    pos = 0
    c = [0]*n

    for i in range(k):
