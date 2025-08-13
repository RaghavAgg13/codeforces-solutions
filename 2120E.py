for i in range(int(input())):
    n, k = list(map(int, input().split()))
    cars = sorted(list(map(int, input().split())), reverse=True)

    angriness = 0
    delta = max(cars) - min(cars) - k - 1

    while delta > 0:
        cars[0] -= 1
        cars[-1] += 1

        angriness += k

        cars.sort(reverse=True)
        delta = cars[0] - cars[-1] - k - 1

    for i in cars:
        angriness += i*(i+1)//2 

    print(angriness)