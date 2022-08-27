coord = input()
x = ord(coord[0]) - ord('a') + 1
y = int(coord[1])
minX, minY, maxX, maxY = 1, 1, 8, 8
count = 0

move = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

for i in move:
    nx = x + i[0]
    ny = y + i[1]
    if nx < minX or nx > maxX or ny < minY or ny > maxY:
        continue
    count += 1

print(count)
