for i in range(int(input())):
    n = int(input())
    a,b = n//3 + n%3 , n//3

    if n%3 == 2:
        a-=2
        b+=1

    print(a,b)
