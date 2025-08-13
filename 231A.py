length = int(input())
solved = 0
for i in range(length):
    count = 0
    solution = list(map(int, input().split(" ")))
    for j in range(3):
        if solution[j] == 1:
            count += 1
    if count >=2:
        solved +=1
print(solved)