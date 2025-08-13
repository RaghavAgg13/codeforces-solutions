t = int(input())

for i in range(t):
    s = input()
    no = int(s[0])
    a = len(s)

    print(int(10*(no-1) + a*(a+1)/2))