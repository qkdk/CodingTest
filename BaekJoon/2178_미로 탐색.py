from collections import deque

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]


# 그래프에서 백 트래킹을 활용한 예
def dfs(coord, count):
    x, y = coord
    count += 1
    if x == m - 1 and y == n - 1:
        answer.append(count)
    for i in move:
        nx, ny = i[0] + x, i[1] + y
        if nx >= m or nx < 0 or ny >= n or ny < 0:
            continue
        if graph[ny][nx] == 0:
            continue
        # 방문했다면
        if visited[ny][nx] == 1:
            continue
        visited[ny][nx] = 1
        dfs((nx, ny), count)
        visited[ny][nx] = 0

    return


# def bfs(start):
#     q = deque()
#     q.append(start)
#
#     while q:
#         x, y = q.popleft()
#
#         for i in move:
#             nx, ny = i[0] + x, i[1] + y
#             if nx >= m or nx < 0 or ny >= n or ny < 0:
#                 continue
#             if graph[ny][nx] == 0:
#                 continue
#             if visited[ny][nx] != 0:
#                 continue
#             q.append((nx, ny))
#             visited[ny][nx] = visited[y][x] + 1
#
#     return


n, m = map(int, input().split())
visited = [[0] * m for _ in range(n)]
start = (0, 0)
graph = []
answer = []
for i in range(n):
    graph.append(list(map(int, input())))

# bfs(start)
dfs(start, 0)
visited[0][0] = 1

print(min(answer))
