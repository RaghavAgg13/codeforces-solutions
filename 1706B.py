alphabets = '-abcdefghijklmnopqrstuvwxyz'

for i in range(int(input())):
    n = int(input())
    l = sorted(list(set(list(input()))))
    print(alphabets.index(l[-1]))