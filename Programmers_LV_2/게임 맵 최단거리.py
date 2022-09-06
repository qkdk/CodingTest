from collections import deque


def solution(maps):
    q = deque()
    q.append((0, 0))
    vector = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + vector[i][0]
            ny = y + vector[i][1]
            if nx >= len(maps[0]) or ny >= len(maps) or nx < 0 or ny < 0:
                continue
            if maps[ny][nx] == 0:
                continue
            if maps[ny][nx] == 1:
                q.append((nx, ny))
                maps[ny][nx] = maps[y][x] + 1

    if maps[-1][-1] == 1 or 0:
        return -1
    else:
        return maps[-1][-1] + 1

# def solution(maps):
#     # 마지막 곳에 도착했을때의 count값을 저장
#     # 도착하지 못하였다면 return -1
#     # 이미 지나간 곳은 0 => 1로 표시로 해결
#     # dfs 와 bfs 를 사용
#     count = 1
#     count += dfs(0, 0, maps, count)
#     answer = 0
#     return answer
#
#
# def dfs(x, y, maps, count):
#     if x == len(maps[0]) and y == len(maps):
#         return count + 1
#
#     vector = [(0, -1), (1, 0), (0, 1), (-1, 0)]
#
#     maps[x][y] = 1
#
#     for i in range(4):
#         nx = x + vector[i][0]
#         ny = y + vector[i][1]
#         if ny > len(maps[0]) or nx > len(maps):
#             break
#         if maps[nx][ny] == 0:
#             flag += 1
#             count += dfs(nx, ny, maps, count)
#
#
#     return count

# => dfs로는 풀기 어렵고 시간이 많이 걸린다.
# 막다른곳이 종점이 아닐 가능성 존재, 이를 처리하는데 시간이 오래걸려 시간복잡도 out
