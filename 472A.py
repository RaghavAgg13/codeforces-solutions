n = int(input())

def get_val(n):
    for i in range(1, n+1):
        for j in range(2, i):
            if i % j == 0:
                for x in range(2, n-i-1):
                    if (n-i) % x == 0:
                        print(i, n-i)
                        return

get_val(n)