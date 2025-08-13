for i in range(int(input())):
    x,y = list(map(int, input().split()))
    a,b = list(map(int, input().split())) 

    x, y = min(x,y), max(x,y)
    
    if x >= 0 and y >= 0:
        score1 = x*b + (y-x)*a
        score2 = y*b + (y-x)*a
        score3 = (x+y)*a

        score = min(score1, score2, score3)
    elif x <= 0 and y <= 0:
        score1 = - x + (x-y)*a
        score2 = - y*b + (x-y)*a

        score = min(score1, score2)
    else:
        score1 = y*b + (y-x)*a
        score2 = -x*b + (y-x)*a
        score3 = (y-x)*a

        score = min(score1, score2, score3)

    print(score)