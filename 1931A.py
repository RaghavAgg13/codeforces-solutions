alp = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(int(input())):
    n = int(input())

    if 3 <= n <= 28:
        print(f'aa{alp[n-2]}')
    elif 29 <= n <= 53:
        print(f'a{alp[n-1-26]}z')
    elif 54 <= n <= 78:
        print(f'{alp[n-26-26]}zz')