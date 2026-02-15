s = input()

if s == "first":
    n = int(input())
    a = list(map(int, input().split()))

    word = ''
    for i in a:
        word += chr(i+96)
    print(word)
else:
    word = input()
    a = []

    print(len(word))
    for i in word:
        a.append(ord(i)-96)
    print(*a)