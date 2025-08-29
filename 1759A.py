for i in range(int(input())):
    a = input()

    while 'YesYes' in a:
        a = a.replace('YesYes', "Yes")

    if a in 'YesYesYes':
        print('YES')
    else: print('NO')
    
    
    
    
    # if 'yesyes' in a:
    #     if a == '' or a in 'yesyes':
    #         print('YES')
    #     else: print('NO')

    # else: print('NO')