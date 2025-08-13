for i in range(int(input())):
    words = list(map(str, input().split()))
    for word in words:
        print(word[0], end='')
    print()