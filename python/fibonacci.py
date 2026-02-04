def fib_recursive(n: int) -> int:
    if n <= 1: return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_dp(n: int) -> int:
    if n <= 1: return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

def fib_generator(n: int):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def fib_matrix(n: int) -> int:
    def matrix_mult(a, b):
        return [[a[0][0]*b[0][0] + a[0][1]*b[1][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]],
                [a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1]]]
    def matrix_pow(m, n):
        if n == 1: return m
        half = matrix_pow(m, n // 2)
        result = matrix_mult(half, half)
        if n % 2: result = matrix_mult(result, m)
        return result
    if n == 0: return 0
    base = [[1, 1], [1, 0]]
    return matrix_pow(base, n)[0][1]

if __name__ == "__main__":
    print([n for n in fib_generator(10)])
    print(fib_matrix(10))
