from collections import deque


def solution(s):
    answer = []
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # 문자열을 파이썬에 알맞은 형태로 변환
    stack_number = []
    stack = []
    tmp_stack = []

    q = deque()
    for i in s:
        q.append(i)

    while q:
        if q[0] == '{':
            stack.append(q[0])
            q.popleft()

        elif q[0] == '}':
            tmp = ''
            for i in tmp_stack:
                tmp += i
            stack_number.append(tmp)
            tmp_stack = []
            stack.append(q[0])
            q.popleft()

        elif q[0] in numbers:
            tmp_stack.append(q[0])
            q.popleft()

        else:
            tmp = ''
            for i in tmp_stack:
                tmp += i
            stack_number.append(tmp)
            tmp_stack = []
            q.popleft()

        if stack[-2:] == ['{', '}']:
            stack.pop()
            stack.pop()
            answer.append(stack_number)
            # print(answer)
            stack_number = []
            # print(answer)

    for i in range(len(answer)):
        if answer[i][0] == '':
            answer[i].pop(0)

    answerList = []

    for i in range(1, len(answer) + 1):
        for j in answer:
            if len(j) == i:
                for k in j:
                    if k not in answerList:
                        answerList.append(k)

    return [int(x) for x in answerList]


# 정답
def solution(s):
    answer = []

    s1 = s.lstrip('{').rstrip('}').split('},{')

    new_s = []
    for i in s1:
        new_s.append(i.split(','))

    new_s.sort(key=len)

    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    # 판별 알고리즘
    return answer


# def solution(s):
#     answer = []
#
#     s1 = s.lstrip('{').rstrip('}').split('},{')
#     print(s1)
#
#     sList = []
#     for i in s1:
#         sList.append(i.split(','))
#
#     print(sList)
#     sList.sort(key=len)
#
#     return answer
#

# solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")
solution("{{20,111},{111}}")
