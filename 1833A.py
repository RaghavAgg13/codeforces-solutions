for i in range(int(input())):
    n = int(input())
    s = input()

    arr = []
    for i in range(n-1):
        if s[i:i+2] not in arr:
            arr.append(s[i:i+2])

    print(len(arr))