# def solution(number, k):
#     maxNum = '0'
#     index = 0
#
#     for i in range(k + 1):
#         if maxNum < number[i]:
#             maxNum = number[i]
#             index = i
#
#     k -= index
#     number = number[index:]
#
#     index = 0
#     while index < len(number) - 1:
#         if number[index] < number[index + 1]:
#             number = number[:index] + number[index + 1:]
#             k -= 1
#
#         if k == 0:
#             break
#         index += 1
#
#     if k > 0:
#         number = number[:-k]
#
#     print(number)
#     return number


def solution(number, k):
    stack = []
    initK = k

    for i in range(len(number)):
        if not stack:
            stack.append(number[i])
            continue

        while stack[-1] < number[i] and k > 0:
            stack.pop()
            k -= 1
            if not stack:
                break
        stack.append(number[i])

        if k == 0:
            break

    if k == 0:
        answer = ''.join(stack) + number[len(stack) + initK:]
    else:
        answer = ''.join(stack)[:-k]

    return answer


# solution("4177252841", 4)
# solution("1924", 2)
# solution("1231234", 3)
# solution("13485301", 4)
solution("4321", 1)
