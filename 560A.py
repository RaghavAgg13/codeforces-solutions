from sys import stdin, stdout
input = stdin.readline

n = int(input())
a = list(map(int, input().split()))

if 1 in a:
    stdout.write("-1")
else:
    stdout.write("1")