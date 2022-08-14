from collections import deque

def solution(s):

    queue = deque(list(s))
    stack = []

    while True:
        if len(queue) == 0: break
        else:
            if len(queue) > 1 and queue[0] == queue[1]:
                queue.popleft()
                queue.popleft()
            else:
                stack.append(queue[0])
                if len(stack)>1 and stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                queue.popleft()

    if len(stack) == 0 and len(queue) == 0 :
        return 1
    else : return 0

solution("cdcd")