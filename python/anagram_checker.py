from collections import Counter

def is_anagram(s1: str, s2: str) -> bool:
    return Counter(s1.lower().replace(" ", "")) == Counter(s2.lower().replace(" ", ""))

def group_anagrams(words: list) -> list:
    groups = {}
    for w in words:
        key = "".join(sorted(w))
        if key not in groups:
            groups[key] = []
        groups[key].append(w)
    return list(groups.values())

if __name__ == "__main__":
    print(is_anagram("listen", "silent"))
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
