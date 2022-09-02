# # bfs
# def solution(numbers, target):
#     answer = 0
#     result = [0]
#     for i in numbers:
#         tmp = []
#         for j in result:
#             tmp.append(j + i)
#             tmp.append(j - i)
#         result = tmp
#
#     for i in result:
#         if i == target:
#             answer += 1
#     return answer
#
#
# solution([1, 1, 1, 1, 1], 3)

# dfs
answer = 0


def dfs(cur_list, array, target):
    depth = len(cur_list)
    global answer
    if len(cur_list) == len(array):
        if target == sum(cur_list):
            answer += 1
            return
        else:
            return

    else:
        for i in [1, -1]:
            tmp_list = cur_list[:]
            tmp_list.append(i * array[depth])
            dfs(tmp_list, array, target)
        return


def solution(numbers, target):
    dfs([], numbers, target)
    return answer


solution([1, 1, 1, 1, 1], 3)
