for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    first_element = a[0]
    possible = True
    
    for i in range(1, n):
        if a[i] % first_element:
            possible = False
            break

    print("YES" if possible else 'NO')