from bisect import bisect_left


def solution(citations):
    answer = 0

    citations.sort()
    for i in range(len(citations) + 1):
        index = bisect_left(citations, i)
        if len(citations[:index]) <= i <= len(citations[index:]):
            answer = i

    print(answer)
    return answer


# solution([3, 0, 6, 1, 5])
# solution([3, 4, 5, 11, 15, 16, 17, 18, 19, 20])
# solution([6, 5, 5, 5, 3, 2, 1, 0])
solution([4, 4, 4])
