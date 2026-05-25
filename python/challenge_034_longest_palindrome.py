"""
Challenge 034: Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Approach: Expand Around Center
- For each character (and each gap between characters), expand outward
  while both ends match.
- Track the longest palindrome found.

Complexity: O(n²) time, O(1) space

Tags: string, two-pointers, dynamic-programming
"""


def longest_palindrome(s: str) -> str:
    """Return the longest palindromic substring in s."""
    if not s:
        return ""

    start, max_len = 0, 0

    def expand(left: int, right: int) -> tuple[int, int]:
        """Expand around center and return (start, length) of palindrome."""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # left and right are now one step past the valid palindrome
        return left + 1, right - left - 1

    for i in range(len(s)):
        # Odd-length palindrome (single char center)
        l, length = expand(i, i)
        if length > max_len:
            start, max_len = l, length

        # Even-length palindrome (between two chars)
        l, length = expand(i, i + 1)
        if length > max_len:
            start, max_len = l, length

    return s[start : start + max_len]


# --- test cases ---
if __name__ == "__main__":
    tests = [
        ("babad", "bab"),           # "aba" also valid
        ("cbbd", "bb"),
        ("a", "a"),
        ("ac", "a"),                # single char
        ("racecar", "racecar"),     # whole string
        ("", ""),
        ("aaaa", "aaaa"),
    ]

    for s, expected in tests:
        result = longest_palindrome(s)
        # For "babad", accept either "bab" or "aba"
        if s == "babad":
            assert result in ("bab", "aba"), f"Got {result}"
        else:
            assert result == expected, f"s={s!r}: expected {expected!r}, got {result!r}"
        print(f"✅ longest_palindrome({s!r}) = {result!r}")

    print("\nAll tests passed!")
