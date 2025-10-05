a,b,c = list(map(int, input().split()))

print(max(max(1+a-b-c,0), max(1+b-c-a, 0), max(1+c-a-b, 0)))