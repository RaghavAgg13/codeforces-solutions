for i in range(int(input())):
    year = int(input())

    if year**0.5 == int(year**0.5):
        year **= 0.5
        year = int(year)

        print(f"1 {year-1}" if year != 0 else '0 0')
    else:
        print(-1)