from collections import Counter
for i in range(int(input())):
    n = int(input())
    a = set(input().split())
    b = set(input().split())
    c = set(input().split())

    scorea,scoreb,scorec = 0,0,0
    for word in a:
        if word not in b and word not in c:
            scorea += 3
        elif (word in b) !=( word in c):
            scorea += 1
        
    for word in b:
        if word not in a and word not in c:
            scoreb += 3
        elif (word in a) != (word in c):
            scoreb += 1
        
    for word in c:
        if word not in a and word not in b:
            scorec += 3
        elif (word in b )!= (word in a):
            scorec += 1
        

    print(scorea,scoreb,scorec)
    del a,b,c