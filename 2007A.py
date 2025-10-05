'''
Any pair which has more than 2 even numbers is invalid
So, any pair is just 3 odd numbers of 2 odd+ 1 even
In general, i can make more 2odd+1even than 3odd pairs
If no of even is greater than i know my pairs are maximized
But, in the other case, i also need to take care of the rem pairs of odd (odd-even*2)
'''

for i in range(int(input())):
    l,r = list(map(int, input().split()))

    odd = r//2+r%2-l//2
    even = r-l+1-odd
    
    if even*2 > odd: n1 = odd//2
    else: n1 = even+(odd-even*2)//3 
    print(n1)