def reverse_string(s: str) -> str:
    return s[::-1]

def reverse_words(s: str) -> str:
    return " ".join(s.split()[::-1])

def is_palindrome(s: str) -> bool:
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    print(reverse_string("hello"))
    print(reverse_words("hello world python"))
    print(is_palindrome("A man, a plan, a canal: Panama"))
