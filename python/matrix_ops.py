def matrix_multiply(a: list, b: list) -> list:
    if len(a[0]) != len(b): raise ValueError("Incompatible dimensions")
    result = [[0] * len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result

def matrix_transpose(m: list) -> list:
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def matrix_rotate(m: list) -> list:
    n = len(m)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n - 1 - i] = m[i][j]
    return result

def matrix_spiral(m: list) -> list:
    if not m: return []
    result = []
    top, bottom, left, right = 0, len(m) - 1, 0, len(m[0]) - 1
    while top <= bottom and left <= right:
        result.extend(m[top][left:right + 1]); top += 1
        for i in range(top, bottom + 1): result.append(m[i][right]); right -= 1
        if top <= bottom: result.extend(m[bottom][left:right + 1][::-1]); bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1): result.append(m[i][left]); left += 1
    return result

if __name__ == "__main__":
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    print(matrix_multiply(a, b))
    print(matrix_spiral([[1,2,3],[4,5,6],[7,8,9]]))
