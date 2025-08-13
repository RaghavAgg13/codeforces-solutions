n = int(input())
_fromPerson = list(map(int, input().split(' ')))
_toPerson = ''
for i in range(1, n+1):
    _toPerson += str(_fromPerson.index(i) + 1) + ' '
print(_toPerson[:-1])