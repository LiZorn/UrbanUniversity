numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

is_prime = True

for i in numbers:
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
        else:
            is_prime = True
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)

print(f"Primes: {primes}")
print(f"Not Primes: {not_primes}")

# Primes: [2, 3, 5, 7, 11, 13]
# Not Primes: [4, 6, 8, 9, 10, 12, 14, 15]

