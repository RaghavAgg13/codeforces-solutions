s = input()
count_lower, count_upper = 0,0
for i in s:
    if str.lower(i) == i:
        count_lower += 1
    elif str.upper(i) == i:
        count_upper += 1
    else:
        continue

if count_lower < count_upper:
    print(str.upper(s))
else:
    print(str.lower(s))