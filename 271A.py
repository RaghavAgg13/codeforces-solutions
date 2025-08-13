y = str ( int(input()) + 1 )
b = False

while b != True:
    if len(set(list(y))) == 4:
        print(y)
        b=True
    else:
        y = str( int(y) + 1)