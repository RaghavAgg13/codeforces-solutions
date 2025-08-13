w1 = 'I hate it'
w2 = 'I love it'

n = int(input())

if n == 1: print(w1)
elif n == 2: print('I hate that I love it')
else:
    for i in range((n-1)//2):
        print('I hate that I love that ', end='')
    if n % 2 == 0:
        print('I hate that I love it')
    else:
        print('I hate it')