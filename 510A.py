n,m = list(map(int, input().split(' ')))
b = False
print('#'*m)

for i in range((n-1)//2):
    if b == False:
        print('.'*(m-1), '#', sep='')
        print('#'*m)
        b = True
    else:
        print('#', '.'*(m-1), sep='')
        print('#'*m)
        b = False