def is_prime(n: int) -> bool:
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True

def primes_up_to(n: int) -> list:
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i, p in enumerate(sieve) if p]

def nth_prime(n: int) -> int:
    count, num = 0, 2
    while True:
        if is_prime(num):
            count += 1
            if count == n: return num
        num += 1

if __name__ == "__main__":
    print(primes_up_to(100))
    print(nth_prime(10))
