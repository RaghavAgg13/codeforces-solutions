a = input()

idx = a.index("^")
left = 0
for i in range(idx):
    if "1" <= a[i] <= "9":
        left += int(a[i])*(idx-i)
right = 0
for i in range(idx+1, len(a)):
    if "1" <= a[i] <= "9":
        right += int(a[i])*(i-idx)

if left == right:
    print('balance')
elif left > right:
    print("left")
else:
    print("right")