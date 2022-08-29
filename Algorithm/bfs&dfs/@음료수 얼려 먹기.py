def dfs(x, y):
    if x < 0 or x >= row or y < 0 or y >= col:
        return False
    if table[x][y] == 0:
        table[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


row, col = map(int, input().split())
table = []

for _ in range(row):
    table.append([int(a) for a in input()])

result = 0

for i in range(row):
    for j in range(col):
        if dfs(i, j):
            result += 1

print(result)
