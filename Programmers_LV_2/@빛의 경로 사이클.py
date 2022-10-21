count = 1


def solution(grid):
    answer = []

    rows = len(grid)
    cols = len(grid[0])
    # 3차원 배열 만들기
    vector_table = [[[0, 0, 0, 0] for x in range(cols)] for x in range(rows)]

    global count

    for i in range(rows):
        for j in range(cols):
            for k in range(4):
                # 북동남서 : 0123
                if dfs(j, i, grid, vector_table, k):
                    if count != 0:
                        answer.append(count)
                    count = 1
    answer.sort()
    return answer


def dfs(x, y, grid, vector_table, k):
    global count
    if vector_table[y][x][k] == 1:
        count = 0
        return True

    vector_table[y][x][k] = 1
    vector = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    nx, ny = 0, 0
    if grid[y][x] == 'R':
        k = (k + 1) % 4
        nx = x + vector[k][0]
        ny = y + vector[k][1]
        # k = 0 => 1
        # k = 1 => 2
        # k = 2 => 3
        # k = 3 => 0
    if grid[y][x] == 'L':
        k = (k + 3) % 4
        nx = x + vector[k][0]
        ny = y + vector[k][1]
        # k = 0 => 3
        # k = 1 => 0
        # k = 2 => 1
        # k = 3 => 2
    if grid[y][x] == 'S':
        k = k
        nx = x + vector[k][0]
        ny = y + vector[k][1]
        # k = 0 => 0
        # k = 1 => 1
        # k = 2 => 2
        # k = 3 => 3

    nx, ny = nx % len(grid[0]), ny % len(grid)
    if vector_table[ny][nx][k] == 1:
        return True
    else:
        count += 1
        dfs(nx, ny, grid, vector_table, k)
        return True


#
# solution(["SL", "LR"])
# solution(["S"])
solution(["S", "S"])
