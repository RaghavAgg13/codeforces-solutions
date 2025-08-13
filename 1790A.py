pi = '314159265358979323846264338327'
for i in range(int(input())):
    t = input()
    count = 0
    for i in range(len(t)):
        if t[i] == pi[i]:
            count += 1
        else:
            print(count)
            break
    
    if count == len(t):
        print(count)