from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= row or ny < 0 or ny >= col:
                continue
            if graph[ny][nx] == 0:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = graph[y][x] + 1
                queue.append((nx, ny))

    return graph[col - 1][row - 1]


col, row = map(int, input().split())

graph = []
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

for _ in range(col):
    graph.append([int(a) for a in input()])

print(bfs(0, 0))
