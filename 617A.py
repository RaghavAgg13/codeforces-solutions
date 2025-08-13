n = int(input())
base = n // 5 

if n%5 != 0:
    base += 1

print(base)