a = input()
n = len(a)

stack = [0]*n
top = 0
cnt = 0

for i in range(n):
    if top > 0 and stack[top-1] in "({[<" and a[i] in ")}]>":
        if (not((stack[top-1] == "(" and a[i] == ")") or (stack[top-1] == "<" and a[i] == ">") or (stack[top-1] == "[" and a[i] == "]") or (stack[top-1] == "{" and a[i] == "}"))): cnt += 1

        top -= 1
    else:
        stack[top] = a[i]
        top += 1
    
if top > 0: print("Impossible")
else: print(cnt)