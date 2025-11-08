n = int(input())
a = input()

x = abs(a.count('U')-a.count('D'))+ abs(a.count('L')-a.count('R'))
print(n-x)