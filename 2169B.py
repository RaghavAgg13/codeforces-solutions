for i in range(int(input())):
    a = input()

    if a == "*": print(1)
    elif "**" in a: print(-1)
    else:
        if ">*" in a or "*<" in a or "><" in a: print(-1)
        else:
            cnt = 0
            cul = 0
            for i in range(len(a)):
                if a[i] == ">":
                    cnt = max(cnt, cul)
                    cul = 0
                else:
                    cul += 1

            cnt = max(cnt, cul) 
            cul = 0
            for i in range(len(a)):
                if a[i] == "<":
                    cnt = max(cnt, cul)
                    cul = 0
                else:
                    cul += 1
            cnt = max(cnt, cul) 
        
            print(cnt)