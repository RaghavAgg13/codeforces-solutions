t = int(input())
output = []
for i in range(t):
    n = int(input())
    no = 0
    for i in range(n):
        no += 1
        # print('no is', no)

        if i != n-1:
            if (no+1) % 3 == 0 or str(no+1)[-1] == '3':
                no += 1
                # print('next no was', no, 'so added 1')
                if (no+1) % 3 == 0 or str(no+1)[-1] == '3':
                    no += 1
                    # print('next to that no was', no, 'so added 1')
            
    print(no)