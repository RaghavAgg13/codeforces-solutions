for j in range(int(input())):
    n = int(input())
    a = list(input().strip())

    left,right = 0, n-1
    flag = 0

    while left < right:
        if a[left] != a[right]:
            for i in range(left, right):
                a[i] = '0' if a[i] == '1' else '1'
            left += 1

            if a == a[::-1]: flag = 0
            else: flag = 1
            break
        else: 
            left += 1
            right -= 1

    print('NO' if flag else 'YES')
