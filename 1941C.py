for i in range(int(input())):
    n = int(input())
    s = input()
    
    count = 0
    i = 0
    while i < n:
        if i + 5 <= n and s[i:i+5] == "mapie":
            count += 1
            i += 5
        elif i + 3 <= n and (s[i:i+3] == "map" or s[i:i+3] == "pie"):
            count += 1
            i += 3
        else:
            i += 1
            
    print(count)