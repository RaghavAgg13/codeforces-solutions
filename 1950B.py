for i in range(int(input())):
    n = int(input())

    s = ''
    s_ = ''
    for i in range(n):
        s += '##' if i%2 == 0 else '..'
        s_ += '..' if i%2 == 0 else '##'

    for i in range(n):
        if i%2 == 0:
            print(s)
            print(s)
        else:
            print(s_)
            print(s_)
