"""Advanced Dynamic Programming Solutions"""
import bisect

def length_of_lis_optimized(nums):
    tails = []
    for n in nums:
        i = bisect.bisect_left(tails, n)
        if i == len(tails):
            tails.append(n)
        else:
            tails[i] = n
    return len(tails)

def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1): dp[i][0] = i
    for j in range(n + 1): dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]

def palindrome_partition(s):
    n = len(s)
    dp = [float("inf")] * (n + 1)
    dp[0] = 0
    is_pal = [[False] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j - i <= 2 or is_pal[i+1][j-1]):
                is_pal[i][j] = True
    for i in range(1, n + 1):
        for j in range(i):
            if is_pal[j][i-1]:
                dp[i] = min(dp[i], dp[j] + 1)
    return dp[n] - 1

if __name__ == "__main__":
    print(length_of_lis_optimized([10, 9, 2, 5, 3, 7, 101, 18]))
    print(edit_distance("horse", "ros"))
    print(palindrome_partition("aab"))
