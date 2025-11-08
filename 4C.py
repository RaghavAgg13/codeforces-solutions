n = int(input())
simmilar = {}
for i in range(n):
    s = input()
    if s in simmilar:
        # simmilar[s + str(simmilar[s])] = 1
        print(s+str(simmilar[s]))
        simmilar[s] += 1
    else:
        print('OK')
        simmilar[s] = 1