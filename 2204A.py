for i in range(int(input())):
    n = int(input())
    a = input()

    pos = 1

    while (pos < n and a[pos] == "R"): pos += 1

    print(pos+1)
    