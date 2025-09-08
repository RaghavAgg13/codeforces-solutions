n = int(input())
a = list(map(int, input().split()))
s1 = sum([a[i] for i in range(0,n,3)])
s2 = sum([a[i%n] for i in range(1,n,3)])
s3 = sum([a[i%n] for i in range(2,n,3)])

if s1 == max(s1,s2,s3):
    print('chest')
elif s2 == max(s1,s2,s3):
    print('biceps')
else:
    print('back')