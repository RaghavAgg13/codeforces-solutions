for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
 
    if n == 1:
        print(l[0])
    else:
        final = 0
        count = 0
        for i in range(n-1):
            if l[i]*l[i+1] < 0:
                final += max(l[i-count:i+1])
                count = 0
            else: count += 1
    
        if count != 0: final += max(l[n-count-1:n])
        # checking last 2 elements because
        # for loop goes till (n-1)th pair
        if l[n-2]*l[n-1] < 0: final += l[-1]
        print(final)