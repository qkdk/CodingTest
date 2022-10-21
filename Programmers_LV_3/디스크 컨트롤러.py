import heapq


def solution(jobs):
    answer = 0

    current_time = 0
    jobs.sort(key=lambda x: x[0], reverse=True)
    q = []
    length = len(jobs)

    while True:
        while jobs:
            job = jobs.pop()
            if job[0] > current_time:
                jobs.append(job)
                break
            heapq.heappush(q, [job[1], job[0]])

        if jobs and not q:
            current_time += 1
            continue
        if not q and not jobs:
            break

        pt, st = heapq.heappop(q)
        current_time = current_time + pt
        answer += current_time - st

    answer = answer // length
    print(answer)

    return answer


# solution([[0, 3], [1, 9], [2, 6]])  # return 9
solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]])  # 72
