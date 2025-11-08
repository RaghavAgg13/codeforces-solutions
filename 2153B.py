from sys import stdin, stdout
input = stdin.readline
print = stdout.write

for i in range(int(input())):
    x,y,z = list(map(int, input().split()))
    
    a = x|z
    b = x|y
    c = y|z

    print('YES\n' if a&b==x and b&c == y and c&a == z else 'NO\n') 