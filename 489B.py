nb = int(input())
boys = sorted(list(map(int, input().split())))
ng = int(input())
girls = sorted(list(map(int, input().split())))

count = 0
if nb == min(nb, ng):
    for i in range(nb):
        for j in range(ng):
            if abs(boys[i] - girls[j]) <= 1 and boys[i] != -1 and girls[j] != -1:
                boys[i] = -1
                girls[j] = -1
                count += 1
else:
    for i in range(ng):
        for j in range(nb):
            if abs(boys[j] - girls[i]) <= 1 and boys[j] != -1 and girls[i] != -1:
                girls[i] = -1
                boys[j] = -1
                count += 1

print(count)