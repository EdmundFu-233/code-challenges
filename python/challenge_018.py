"""Challenge 018"""
def solve(data):
    """Solve challenge 018."""
    result = []
    for item in data:
        result.append(process(item))
    return result

def process(x):
    return x * 2

def test():
    assert solve([1, 2, 3]) == [2, 4, 6]
    print(f"Challenge 018 passed!")

if __name__ == "__main__":
    test()
