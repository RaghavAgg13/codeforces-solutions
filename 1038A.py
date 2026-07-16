n,k = list(map(int, input().split()))
a = input()

freq = [0]*k

for i in a:
    freq[ord(i)-ord('A')] += 1

ans = n
for i in range(k):
    ans = min(ans, freq[i])

print(ans*k)