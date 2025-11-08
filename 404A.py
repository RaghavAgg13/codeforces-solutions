n = int(input())

check = True
sem = ""
other = ""
for i in range(n):
    a = input()

    if sem == "": sem = a[0]
    if other == "": other = a[1]

    if sem == other:
        check = False

    if check:
        for j in range(n):
            if (i == j or i+j == n-1):
                if a[j] != sem:
                    check = False
                    break
            elif i != j:
                if a[j] != other:
                    check = False
                    break

print('YES' if check else 'NO')