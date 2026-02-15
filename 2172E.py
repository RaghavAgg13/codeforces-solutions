pos = [[], [12, 21], [123, 132, 213, 231, 312, 321], [1234, 1243, 1324, 1342, 1423, 1432, 2134, 2143, 2314, 2341, 2413, 2431, 3124, 3142, 3214, 3241, 3412, 3421, 4123, 4132, 4213, 4231, 4312, 4321]]

for i in range(int(input())):
    n,j,k = list(map(int, input().split()))
    n = len(set(str(n)))-1
    n1 = str(pos[n][j-1])
    n2 = str(pos[n][k-1])

    # print(n1, n2)
    x = 0
    for i in range(n+1):
        if n1[i] == n2[i]: x += 1
    
    print(f"{x}A{n+1-x}B")