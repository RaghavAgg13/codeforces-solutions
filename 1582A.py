for i in range(int(input())):
    a,b,c = list(map(int, input().split()))
    times = [a,b*2,c*3]

    print(sum(times)%2)