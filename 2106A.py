for i in range(int(input())):
    n = int(input())
    s = input()
 
    count1 = s.count('1')
    count2 = n-count1
 
    final = count1*(count1-1)+count2*(count1+1)
    print(final)