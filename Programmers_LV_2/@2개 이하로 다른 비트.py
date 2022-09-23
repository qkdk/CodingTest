# def solution(numbers):
#     answer = []
#
#     for num in numbers:
#         count = 0
#         tmp = num
#         num_str = str(bin(num))
#
#         while True:
#             tmp += 1
#             tmp_str = str(bin(tmp))
#
#             if len(tmp_str) > len(num_str):
#                 num_str = num_str[:2] + '0' + num_str[2:]
#
#             for i in range(len(num_str)):
#                 if num_str[i] != tmp_str[i]:
#                     count += 1
#
#             if 3 > count > 0:
#                 answer.append(tmp)
#                 break
#
#             count = 0
#
#     return answer

def solution(numbers):
    answer = []

    for number in numbers:
        str_number = '0' + str(bin(number))[2:]
        if str_number[-1] == '0':
            answer.append(int(str_number[: -1] + '1', 2))
            continue

        for i in range(len(str_number) - 1, -1, -1):
            if str_number[i] == '0':
                str_number = str_number[:i] + '10' + str_number[i + 2:]
                answer.append(int(str_number, 2))
                break

    return answer


solution([2, 7])
