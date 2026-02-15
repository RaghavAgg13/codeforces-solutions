a = input()

n = len(a)

stack = [""]*n
top = 0

for i in range(n):
    if (top == 0 or stack[top-1] != a[i]): 
        stack[top] = a[i]
        top += 1
    elif (top > 0 and stack[top-1] == a[i]): 
        top -= 1

if top == 0: print("YES")
else: print("NO")