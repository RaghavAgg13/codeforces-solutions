n = int(input())
l = [[n,n]]
count = 0

while l != []:
    for i in l:
        if 1 in i:
            count += 1
        else:
            a = [i[0]-1, i[1]]
            b = [i[0], i[1]-1]

            if 1 in a: count += 1
            else: l.append(a)
            if 1 in b: count += 1
            else: l.append(b)

        l.remove(i)

print(count)