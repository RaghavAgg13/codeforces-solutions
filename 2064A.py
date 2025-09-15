for i in range(int(input())):
    n = int(input())
    a = input()
    
    check = 0
    if a[0] == '1': check += 1

    count = 0
    for i in range(n-1):
        if a[i] != a[i+1]:
            count += 1
    
    print(count+check)