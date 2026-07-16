n = int(input())
a = input()

cnt = a.count('8')

print(min(n//11, cnt))