import math

def solution(progresses, speeds):
    answer = []
    queue = []

    for i in range(len(progresses)):
        queue.append(math.ceil((100-progresses[i])/speeds[i]))

    while queue !=[]:
        queue = [x-queue[0] for x in queue]
        count = 0
        while queue != [] and queue[0] <1:
            queue.pop(0)
            count += 1
        answer.append(count)

    return answer

solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])