for i in range(int(input())):
    a = input()

    print(25*(ord(a[0])-97) + (ord(a[-1])-96 if a[-1] <= a[0] else ord(a[-1])-97))