for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    print(max(a)+(sum(a)-max(a))/(n-1))