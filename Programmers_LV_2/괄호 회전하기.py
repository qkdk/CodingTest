from collections import deque


def solution(s):
    q = deque(s)
    check_char = [['[', ']'], ['{', '}'], ['(', ')']]

    count = 0
    for i in range(len(q)):
        q.append(q.popleft())

        stack = []
        tmp_q = q.copy()

        for _ in range(len(q)):
            stack.append(tmp_q.popleft())
            if stack[-2:] in check_char:
                stack.pop()
                stack.pop()

        if len(stack) == 0:
            count += 1

    return count


solution("[](){}")
