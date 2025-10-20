for i in range(int(input())):
    n = int(input())

    print((n//2)*5+(n%2)*5 if n>6 else 15)