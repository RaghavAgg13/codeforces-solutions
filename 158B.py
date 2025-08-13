n = int(input())
s1 = list(map(int, input().split(' ')))
 
w_1 = s1.count(1)
w_2 = s1.count(2)
w_3 = s1.count(3)
count = s1.count(4)

#removing groups of 3 and 1
a =  min(w_3, w_1)
w_3 -= a
w_1 -= a
#adding the groups and any spare only 3 groups (1 not present anymore)
count += a + w_3
 
#adding groups containing two 2's
count += w_2//2
w_2 %= 2
 
if w_2 == 1:
    count += w_2
    w_2 = 0
 
    if w_1 >= 2:
        w_1 -= 2
 
    else:
        w_1 = 0
 
while w_2 == 0 and w_1>=1:
    if w_1 >=4:
        count += w_1//4
        w_1 %= 4
    else:
        count += 1
        w_1 = 0
 
print(count)