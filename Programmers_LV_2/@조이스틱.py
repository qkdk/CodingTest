# def solution(name):
#     answer = 0
#
#     return answer
#
#
# def check_alpha(alpha):
#     return min(ord(alpha) - ord('A'), ord('Z') - ord(alpha) + 1)
#
#
# # solution("JEROEN")
# solution("JAN")


# def solution(name):
#     change = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
#     idx = 0
#     answer = 0
#
#     while True:
#         answer += change[idx]
#         change[idx] = 0
#         if sum(change) == 0:
#             return answer
#
#         left, right = 1, 1
#         while change[idx - left] == 0:
#             left += 1
#         while change[idx + right] == 0:
#             right += 1
#
#         answer += left if left < right else right
#         idx += -left if left < right else right
#
#
# solution("JEROEN")


def solution(name):
    answer = 0

    min_move = len(name) - 1

    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        min_move = min([min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next)])

    answer += min_move

    return answer