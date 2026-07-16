from sys import stdout  

x = 1
while x < (1<<29):
    if x%2: x = x*2
    else: x = x*2+1

for _ in range(int(input())):
    print(x); stdout.flush()
    o = int(input())

    m0,m1 = 0, 123456789
    print(m0, m1); stdout.flush()

    v = int(input())

    # v&x == 0 means and and 0
    if ((v&x) == o or (v|x) == o):
        print(0)
    else:
        print(1)
    stdout.flush()