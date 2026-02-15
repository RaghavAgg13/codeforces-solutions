for i in range(int(input())):
    n = int(input())
    s = input()

    if list(s) == sorted(s): print("Bob")
    else:
        print("Alice")
        t = sorted(s)
        cnt = 0
        arr = []
        for i in range(n):
            if s[i] != t[i]:
                cnt += 1
                arr.append(i+1)
        
        print(cnt)
        print(*arr)