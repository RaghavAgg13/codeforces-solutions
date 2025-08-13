a,b = list(map(int, input().split()))
count = a
burnt = a
while burnt >= b:
    count += burnt//b
    burnt -= (burnt//b)*b - burnt//b
print(count)