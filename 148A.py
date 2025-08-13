# rev1: via dictionary
k,l,m,n,d = int(input()), int(input()), int(input()), int(input()), int(input())
# dragon = {}
# for i in range(d):
#     dragon[i] = []
count = 0

# if 1 in [k,l,m,n]:
#   for i in range(d):
#     dragon[i].append('1')  
    
# else:
#     for i in range(1, d):
#         if i*k <= d:
#             dragon[i*k-1].append('w1')
#         if i*l <= d:
#             dragon[i*l-1].append('w2')
#         if i*m <= d:
#             dragon[i*m-1].append('w3')
#         if i*n <= d:
#             dragon[i*n-1].append('w4')
        
 
# for i in dragon.values():
#     if len(i) >= 1:
#         count += 1
# print(count)

#rev2: via list
dragon = [False]*d

if 1 in [k,l,m,n]:
  count = d
else:
    for i in [k, l, m, n]:
       if i <=d:
          for j in range(i-1, d, i):
             if dragon[j] == False:
                dragon[j] = True
                count += 1
        
 
print(count)