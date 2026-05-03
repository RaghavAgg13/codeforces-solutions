for i in range(int(input())):
    n = int(input())
    a = list(input())

    stack = ["" for i in range(n)]

    top = 0
    for i in range(n):
        stack[top] = a[i]
        top += 1

        while (top > 1 and stack[top-1] == stack[top-2]):
            top -= 2
        
    if top == 0:
        print("YES")
    else:
        print("NO")