# from collections import deque
#
#
# def solution(m, n, puddles):
#     answer = 0
#     q = deque()
#     graph = [[0] * m for _ in range(n)]
#     move = [(1, 0), (0, 1)]
#     for coord in puddles:
#         x, y = coord
#         graph[y - 1][x - 1] = -1
#
#     q.append((0, 0))
#
#     while q:
#         y, x = q.popleft()
#
#         for i in move:
#             ny = y + i[0]
#             nx = x + i[1]
#             if ny >= n or nx >= m or ny < 0 or nx < 0:
#                 continue
#             if graph[ny][nx] == -1:
#                 continue
#             graph[ny][nx] = graph[ny][nx] + 1
#             q.append((ny, nx))
#
#     return graph[n - 1][m - 1] % 1000000007


def solution(m, n, puddles):
    graph = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                graph[i][j] = -1
            if j == 0:
                graph[i][j] = -1

    for coord in puddles:
        x, y = coord
        graph[y][x] = -1

    graph[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            left_value = graph[i][j - 1]
            up_value = graph[i - 1][j]

            if graph[i][j] == -1:
                continue
            if left_value != -1 and up_value != -1:
                graph[i][j] = left_value + up_value
            elif left_value == -1 and up_value != -1:
                graph[i][j] = up_value
            elif left_value != -1 and up_value == -1:
                graph[i][j] = left_value

    return graph[n][m] % 1000000007


solution(4, 3, [[2, 2]])
