for i in range(int(input())):
    n,m = list(map(int, input().split()))
 
    negatives = 0
 
    pos, neg = [], []
    for i in range(n):
        a = list(map(int, input().split()))
 
        for no in a:
            if no >= 0: pos.append(no)
            else: neg.append(no)
 
    # print(pos, neg)
 
    if not len(neg)%2 or 0 in pos:
        print(sum(pos)-sum(neg))
    else:
        if pos == []:
            print(sum(pos)-sum(neg)+2*max(neg))
        else:
            if min(pos) == min(min(pos), -1*max(neg)):
                print(sum(pos)-sum(neg)-2*min(pos))
            else:
                print(sum(pos)-sum(neg)+2*max(neg))