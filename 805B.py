from sys import stdout
n = int(input())

if not n%4: stdout.write("aabb"*(n//4))
elif n%4 == 1: stdout.write("aabb"*(n//4)+'a')
elif n%4 == 2: stdout.write("aabb"*(n//4)+'aa')
elif n%4 == 3: stdout.write("aabb"*(n//4)+'aab')