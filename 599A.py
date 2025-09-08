d1,d2,d3 = list(map(int, input().split()))

print(min(d1,d2)+min(max(d1,d2), d3+min(d1,d2))+min(d1+d2, d3))