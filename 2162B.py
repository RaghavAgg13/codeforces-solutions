from sys import stdin, stdout
input = stdin.readline
print = stdout.write
 
for i in range(int(input())):
    n = int(input())
    a = input()
 
    indices = []
    for i in range(n):
        if a[i] == '1':
            indices.append(i+1)
    
    print(str(len(indices))+"\n")
    print(' '.join(str(x) for x in indices)+"\n")