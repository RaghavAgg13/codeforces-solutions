for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    if 0 in a:
        b = a.copy()
        score = 0
        d = 0
        while True:
            for i in range(len(a)+1):
                if i not in a:
                    if i == n: d = i-1
                    score += i
                    break
                else: a.remove(i)
            if 0 not in a: break
 
        score += sum(a)
        print(max(score, sum(b), 2*d, b.count(0)+sum(b)))
    else:
        print(sum(a))
