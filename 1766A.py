for i in range(int(input())):
    n = input().strip()
    first_digit = int(n[0])
    length = len(n)
    count = (length - 1) * 9 + first_digit
    print(count)
