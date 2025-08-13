n,m = list(map(int, input().split(' ')))
house_nos = list(map(int, input().split(' ')))
time = house_nos[0]-1
for i in range(1, m):
    if house_nos[i] < house_nos[i-1]:
        time += n-house_nos[i-1]+house_nos[i]
    elif house_nos[i] > house_nos[i-1]:
        time += house_nos[i] - house_nos[i-1]
    else:
        time += 0
        
print(time)