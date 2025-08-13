id = input()
id_ = []

for i in range(len(id)):
    if id[i] not in id_:
        id_.append(id[i])

if len(id_) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")