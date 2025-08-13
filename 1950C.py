for i in range(int(input())):
    time = input()
    hr = int(time[0:2])
    min = time[3:5]

    if hr > 12:
        if hr <= 21 :
            print(f'0{hr - 12}:{min} PM')
        else:
            print(f'{hr-12}:{min} PM')
    elif hr == 12:
        print(f'12:{min} PM')
    elif hr == 0:
        print(f'12:{min} AM')
    else:
        print(f'{time} AM')