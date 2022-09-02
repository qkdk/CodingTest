from collections import deque


def solution(s):
    answer = True

    queue = deque(list(s))
    stack = []
    while queue:
        stack.append(queue.popleft())
        if stack[-2:] == ['(', ')']:
            stack.pop()
            stack.pop()

    if len(stack) > 0:
        answer = False

    return answer


solution("()()")
