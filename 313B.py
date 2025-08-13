s = input()
check = [0]*len(s)
for i in range(1, len(s)):
    check[i] = check[i-1] + (s[i] == s[i-1])

for i in range(int(input())):
    li, ri = list(map(int, input().split()))        

    count = check[ri-1] - check[li-1]
    print(count)