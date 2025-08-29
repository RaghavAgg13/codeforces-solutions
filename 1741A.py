for i in range(int(input())):
    a,b = list(map(str, input().split()))

    if a[-1] == 'S' and (b[-1] == 'L' or b[-1] == 'M'):
        print("<")
    elif a[-1] == 'M' and (b[-1] == 'L'):
        print("<")
    elif a[-1] == 'M' and (b[-1] == 'S'):
        print(">")
    elif a[-1] == 'L' and (b[-1] == 'S' or b[-1] == 'M'):
        print(">")
    else:
        if len(a) > len(b):
            print(">" if a[-1] != 'S' else "<")
        elif len(a) < len(b):
            print("<" if a[-1] != 'S' else ">")
        else:
            print("=")