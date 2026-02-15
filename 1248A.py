for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    o = sum([i%2 for i in a])
    e = n-o

    n = int(input())
    a = list(map(int, input().split()))

    o_ = sum([i%2 for i in a])
    e_ = n-o_

    print(o*o_+e*e_)