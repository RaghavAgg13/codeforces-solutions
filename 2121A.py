for i in range(int(input())):
    n,s = list(map(int, input().split()))
    a = list(map(int, input().split()))

    if min(a) <= s <= max(a):
        w1 = (max(a)-s)*2+s-min(a)
        w2 = (s-min(a))*2+max(a)-s
        print(min(w1, w2))
    elif s > max(a):
        print(s-min(a))
    else:
        print(max(a)-s)