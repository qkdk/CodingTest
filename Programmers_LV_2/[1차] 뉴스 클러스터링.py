import re
from collections import deque


def make_stack(string):
    exp = re.compile('[a-z]')
    tmp_stack = []

    for i in range(len(string)):
        tmp_string = string[i:i + 2]
        flag = 0
        for j in tmp_string:
            if not exp.match(j):
                flag += 1
        if flag == 0 and len(tmp_string) == 2:
            tmp_stack.append(tmp_string)
        flag = 0

    return tmp_stack


def solution(str1, str2):
    str1 = str.lower(str1)
    str2 = str.lower(str2)

    stack1 = make_stack(str1)
    stack2 = make_stack(str2)

    if stack1 == stack2 == []:
        return 65536

    stack_and = []

    q1 = deque(stack1)
    q2 = deque(stack2)
    q1_count, q2_count = 0, 0

    while True:
        while True:
            if q2_count == len(q2) or len(q1) == 0:
                break
            if q1[0] == q2[0]:
                stack_and.append(q1[0])
                q1.popleft()
                q2.popleft()
                q2_count = 0
            else:
                q2.append(q2[0])
                q2.popleft()
                q2_count += 1
        if q1_count == len(q1):
            break
        q2_count = 0
        q1.append(q1[0])
        q1.popleft()
        q1_count += 1

    num_and = len(stack_and)
    num_sum = len(stack1) + len(stack2) - num_and

    answer = int(num_and / num_sum * 65536)

    return answer

# solution('FRANCE', 'french')
# solution('aa1+aa2', 'AAAA12')
# solution('handshake', 'shake hands')
# solution('E=M*C^2', 'e=m*c^2')
