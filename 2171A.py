for i in range(int(input())):
    n = int(input())

    if n%2: 
        print(0)
        continue
    
    else:
        pairs = n//2 + 1
        print(pairs//2 + pairs%2)