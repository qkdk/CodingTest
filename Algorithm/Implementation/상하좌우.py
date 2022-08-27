n = int(input())
move = input().split()

dic = {'R': 0, 'L': 1, 'D': 2, 'U': 3}

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
x, y = 0, 0
maxX, maxY = n - 1, n - 1

for i in move:
    nx = x + dx[dic[i]]
    ny = y + dy[dic[i]]
    if nx < 0 or nx > maxX or ny < 0 or ny > maxY:
        continue
    x, y = nx, ny

print(nx + 1, ny + 1)
