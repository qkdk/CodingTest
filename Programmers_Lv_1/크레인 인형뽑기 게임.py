def solution(board, moves):

    chamber = [0 for i in range(len(moves))]
    chamberIndex = 0
    answer = 0
    # 인형을 뽑아내는 부분
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                chamber[chamberIndex] = board[j][i-1]
                chamberIndex += 1
                board[j][i-1] = 0

                #인형을 지우는 부분
                if chamber[chamberIndex-1] == chamber[chamberIndex-2]:
                    chamber[chamberIndex-1] = 0
                    chamber[chamberIndex-2] = 0
                    chamberIndex -= 2
                    answer += 2
                break

    return answer

board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

solution(board,moves)