n = int(input())
nos = list(map(int, input().split(' ')))
# for i in nos:
#     count = 0
#     for j in range(1, int(i ** 0.5) + 1):
#         if count <= 3:
#             if i % j == 0: 
#                 count += 1
#                 if j != i // j: count += 1
#         else: break  
#     print('YES' if count == 3 else 'NO')

def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    return {p*p for p, prime in enumerate(is_prime) if prime}

prime_squares = sieve(int(max(nos) ** 0.5) + 1)

for i in nos:
    print('YES' if i in prime_squares else 'NO')