a = input()
b = input()

h1,m1 = int(a[:2]), int(a[3:])
h2,m2 = int(b[:2]), int(b[3:])

t1 = h1*60+m1
t2 = h2*60+m2

if t2 >= t1:
    mid = t1+(t2-t1)//2
else:
    mid = t2 + (t1-t2)//2

    
h,m = mid//60, mid%60
print(f"{h:02d}:{m:02d}")