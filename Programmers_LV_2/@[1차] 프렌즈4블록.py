from collections import deque


def solution(m, n, board):
    answer = 0
    arr_board = deque()

    for i in board:
        tmp = list(i)
        arr_board.append(tmp)

    arr_board = deque(list(zip(*arr_board)))

    while True:
        coord_set = set()
        for i in range(len(arr_board) - 1):
            for j in range(len(arr_board[0]) - 1):
                if arr_board[i][j] == 0:
                    continue
                if arr_board[i][j] == arr_board[i + 1][j] == arr_board[i][j + 1] == arr_board[i + 1][j + 1]:
                    coord_set.add((i, j))
                    coord_set.add((i + 1, j))
                    coord_set.add((i, j + 1))
                    coord_set.add((i + 1, j + 1))

        if len(coord_set) == 0:
            break

        tmp_board = deque([])
        for i in range(len(arr_board)):
            tmp = deque()
            for j in range(len(arr_board[0])):
                if (i, j) in coord_set:
                    tmp.appendleft(0)
                else:
                    tmp.append(arr_board[i][j])
            tmp_board.append(tmp)

        arr_board = tmp_board
        answer += len(coord_set)

    return answer


solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])
