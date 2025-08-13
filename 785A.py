n = int(input())
count = 0
for i in range(n):
    str = input()
    if str == 'Tetrahedron':
        count += 4
    elif str == 'Cube':
        count += 6
    elif str == 'Dodecahedron':
        count += 12
    elif str == 'Icosahedron':
        count += 20
    else:
        count += 8
print(count)