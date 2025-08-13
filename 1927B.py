alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    s = ''
    count0 = 0
    freq = {}

    if sum(a) == n*(n-1)//2:
        s += alp[0]*n
    else:
        for i in a:
            if i == 0:
                ch = alp[count0] 
                count0 += 1       
            else:
                for ch in s:
                    if freq[ch] == i:
                        break
            s += ch
            freq[ch] = freq.get(ch, 0) + 1

    print(s)