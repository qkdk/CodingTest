def solution(board):
    if 1 in list(zip(*board))[0] or 1 in board[0]:
        maxNum = 1
    else:
        maxNum = 0

    for i in range(1, len(board)):  # y
        for j in range(1, len(board[0])):
            if board[i][j] == 0:
                continue
            board[i][j] = min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1
            if maxNum < board[i][j]:
                maxNum = board[i][j]

    return maxNum ** 2


solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]])  # A : 9
