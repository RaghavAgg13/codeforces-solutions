# import pandas as pd
# r1 = list(map(int, input().split(" ")))
# r2 = list(map(int, input().split(" ")))
# r3 = list(map(int, input().split(" ")))
# r4 = list(map(int, input().split(" ")))
# r5 = list(map(int, input().split(" "))) 

# df = pd.DataFrame([r1, r2, r3, r4, r5])
# steps = 0

# for i in range(5):
#     for j in range(5):
#         if df.iat[i, j] == 1:
#             steps = abs(2-i) + abs(2-j)
# print(steps)

# without pandas
r1 = list(map(int, input().split(" ")))
r2 = list(map(int, input().split(" ")))
r3 = list(map(int, input().split(" ")))
r4 = list(map(int, input().split(" ")))
r5 = list(map(int, input().split(" "))) 
steps = 0
for i in range(5):
    if r1[i] == 1:
        steps =  (2 + abs(2-i))
    elif r2[i] == 1:
        steps =  (1 + abs(2-i))
    elif r3[i] == 1:
        steps =  (0 + abs(2-i))
    elif r4[i] == 1:
        steps =  (1 + abs(2-i))
    elif r5[i] == 1:
        steps =  (2 + abs(2-i))
print(steps)    