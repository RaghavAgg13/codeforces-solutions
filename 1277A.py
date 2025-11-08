from sys import stdin, stdout
input = stdin.readline
print = stdout.write

for i in range(int(input())):
    n = int(input())

    a = len(str(n))-1
    cnt = a*9 + n//int('1'*(a+1))

    print(str(cnt)+'\n')