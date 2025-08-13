n= int(input())
w1 = list(map(int, input().split(" ")))[1:]
w2 = list(map(int, input().split(" ")))[1:]
w = sorted(list(dict.fromkeys(w1+w2)))
lvls = [range(1, n+1)]
 
if all(items in w for items in lvls):
    print('I become the guy.')
else:
    print('Oh, my keyboard!')