# def solution(n):
#     answer = 0
#
#     # n만큼만 반복
#     for i in range(n):
#
#     return answer


#
# def solution(n):
#     cases = [0]
#     def dfs(queens, next_queen):
#         # column check
#         if next_queen in queens:
#             return
#
#         for row, column in enumerate(queens):
#             h = len(queens) - row
#             if next_queen == column + h or next_queen == column - h:
#                 return
#
#         queens.append(next_queen)
#
#         if len(queens) == n:
#             cases[0] += 1
#             return
#
#         for next_queen in range(n):
#             dfs(queens[:], next_queen)
#
#     for next_queen in range(n):
#         # 0,1,2,3
#         queens = []
#         dfs(queens, next_queen)
#
#     return cases[0]

# def dfs(queen, row, n):
#     count = 0
#     if n == row:
#         return 1
#     for col in range(n):
#         queen[row] = col
#         for i in range(row):
#             # 같은 col 일 경우
#             if queen[i] == queen[row]:
#                 break
#             # 대각선일 경우
#             if abs(queen[i] - queen[row]) == row -i:
#                 break
#             else:
#                 count += dfs(queen, row + 1, n)
#     return count
#
# def solution(n):
#     return dfs([0]*n, 0, n)



def dfs(queen, row, n):
    count = 0
    if n == row:
        return 1

    for col in range(n):
        queen[row] = col
        for r in range(row):
            if queen[r] == queen[row]:
                break
            if abs(queen[r]-queen[row]) == row - r:
                break
        else:
            count += dfs(queen, row + 1, n)
    return count

def solution(n):
    return dfs([0] * n, 0, n)


solution(4)
