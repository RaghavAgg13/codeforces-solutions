t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    db = []
    score = 0
    for i in s:
        if i not in db:
            db.append(i)
            score += 2
        else: score += 1
    
    print(score)
