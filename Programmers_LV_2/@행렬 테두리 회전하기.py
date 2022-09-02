def solution(rows, columns, queries):
    table = []
    temp_table = [x for x in range(1, rows * columns + 1)]
    answer = []

    for i in range(rows):
        table.append(temp_table[i * columns: i * columns + columns])

    for y_min, x_min, y_max, x_max, in queries:
        # 좌표와 인덱스 맞추기
        y_min -= 1
        x_min -= 1
        y_max -= 1
        x_max -= 1

        tmp = table[y_min][x_min]
        min_number = tmp

        # 서
        for i in range(y_min, y_max):
            table[i][x_min] = table[i + 1][x_min]
            min_number = min(min_number, table[i + 1][x_min])

        for i in range(x_min, x_max):
            table[y_max][i] = table[y_max][i + 1]
            min_number = min(min_number, table[y_max][i + 1])

        for i in range(y_max, y_min, -1):
            table[i][x_max] = table[i - 1][x_max]
            min_number = min(min_number, table[i - 1][x_max])

        for i in range(x_max, x_min, -1):
            table[y_min][i] = table[y_min][i - 1]
            min_number = min(min_number, table[y_min][i - 1])

        table[y_min][x_min + 1] = tmp

        answer.append(min_number)
    return answer


solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]])
