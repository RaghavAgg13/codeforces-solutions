# for i in range(int(input())):
#     n = int(input())
#     a = n

#     mult = []
#     map = {}
#     for i in range(2, int(n**.5)+1):
#         if n%i == 0:
#             map[i] = 1

#             while n%i == 0:
#                 n //= i
#                 map[i] += 1
    
#     if n != 1: map[n] = 1

#     mult = 1
#     for num,freq in enumerate(map):
#         if freq <= n:
#             mult *= num
#         else:
#             mult *= num*(freq//n+freq%n) 
    
#     print(mult)


for _ in range(int(input())):
    n = int(input())

    mult = 1
    for i in range(2, int(n**.5)+1):
        if n%i == 0:
            mult *= i
            while n%i == 0: n //= i
    
    if n != 1: mult *= n

    print(mult)