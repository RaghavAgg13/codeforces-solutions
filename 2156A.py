for i in range(int(input())):
    n = int(input())

    eaten = 0
    while n >= 3:
        eaten += n//3
        n = n//3 + n%3

    print(eaten)