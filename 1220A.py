from math import exp2
n = int(input())
a = input()

x = a.count('n')
y = a.count('z')

print('1 '*x+'0 '*y, sep='')