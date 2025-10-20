for i in range(int(input())):
    n = int(input())
    a = input()
    b = input()
 
    count = 0
    pair = []
    i = 0
    while i < n:
        pair = [a[i], b[i]]
        if '0' in pair:
            if '1' in pair:
                count += 2
            elif i < n-1:
                if a[i+1] == '1' and b[i+1] == '1':
                    count += 2
                    i += 1
                elif a[i+1] == '0' and b[i+1] == '0':
                    count += 1
                else: count += 1
            else:
                count += 1
        else:
            if i < n-1:
                if a[i+1] == '0' and b[i+1] == '0':
                    count += 2
                    i += 1
 
        i += 1
 
    print(count)