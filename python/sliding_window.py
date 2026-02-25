def max_sum_subarray(nums, k):
    if len(nums) < k: return None
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum

def longest_substring(s):
    char_set = set()
    l = max_len = 0
    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l]); l += 1
        char_set.add(s[r])
        max_len = max(max_len, r - l + 1)
    return max_len

def min_window(s, t):
    from collections import Counter
    need = Counter(t); have = {}
    need_count = len(need); have_count = 0
    l = 0; result = (0, float("inf"))
    for r in range(len(s)):
        c = s[r]; have[c] = have.get(c, 0) + 1
        if c in need and have[c] == need[c]: have_count += 1
        while have_count == need_count:
            if r - l < result[1] - result[0]:
                result = (l, r)
            have[s[l]] -= 1
            if s[l] in need and have[s[l]] < need[s[l]]: have_count -= 1
            l += 1
    return s[result[0]:result[1] + 1] if result[1] != float("inf") else ""

if __name__ == "__main__":
    print(max_sum_subarray([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print(longest_substring("abcabcbb"))
