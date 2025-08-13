t = int(input())
count_1, count_2 = 0,0
database = {}
for i in range(t):
    team = input()
    if team not in database:
        database[team] = 1
    elif team in database:
        database[team] += 1
# print(database)
# print(database.values())
count_1 = list(database.values())[0]

if len(database) == 1:
    print(list(database.keys())[list(database.values()).index(count_1)])
else:
    count_2 = list(database.values())[1]
    print(list(database.keys())[list(database.values()).index(count_1)] if count_1 > count_2 else list(database.keys())[list(database.values()).index(count_2)])
    