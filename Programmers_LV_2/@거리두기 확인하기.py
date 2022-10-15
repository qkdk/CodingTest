from collections import deque


def solution(places):
    answer = []

    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for place in places:
        flag = False
        memory_table = [[0 for _ in range(5)] for _ in range(5)]
        for i in range(len(place)):
            if flag:
                break
            for j in range(len(place[0])):
                if flag:
                    break
                if place[i][j] == 'P':
                    q = deque()
                    q.append((i, j, 0))
                    while q:
                        y, x, depth = q.popleft()
                        memory_table[y][x] = 1
                        if depth > 2:
                            continue
                        if place[y][x] == 'X':
                            continue
                        if place[y][x] == 'P' and depth != 0:
                            flag = True
                            break
                        # print(y, x, depth)
                        # 상 하 좌 우
                        for move in moves:
                            dy, dx = move
                            # print(dy, dx)
                            ny, nx = y + dy, x + dx
                            if ny < 0 or ny > 4 or nx < 0 or nx > 4:
                                continue
                            if memory_table[ny][nx] == 1:
                                continue
                            q.append((ny, nx, depth + 1))
        if flag:
            answer.append(0)
        else:
            answer.append(1)

    return answer


solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
