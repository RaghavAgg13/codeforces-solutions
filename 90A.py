r,g,b = list(map(int, input().split()))

mr, mg, mb = r//2+r%2, g//2+g%2, b//2+b%2

m1 = mr*3-3
m2 = 1+mg*3-3
m3 = 2+mb*3-3

# print(m1,m2,m3)
print(max(m1,m2,m3)+30)