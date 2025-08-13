for i in range(int(input())):
    n,k,q = list(map(int, input().split()))
    a = list(map(int, input().split()))
 
    count = 0
    def work(b,c):
        return (b-c+1)*(b-c+2)//2
        
    
    working = 0
    for i in a:
        if i <= q:
            working += 1
        else:
            if working >= k:
                count += work(working,k)
            working = 0
 
    if working >= k:
        count += work(working,k)
 
    print(count)