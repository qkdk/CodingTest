from itertools import combinations_with_replacement


def solution(n, info):
    answer = [-1]
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    info.reverse()
    max_gap = 0

    combi = list(combinations_with_replacement(numbers, n))
    # combi.reverse()

    for c in combi:
        gap = 0
        lion_info = [0] * 11
        for i in c:
            lion_info[i] += 1

        for i in range(11):
            if lion_info[i] == 0 and info[i] == 0:
                continue
            elif info[i] < lion_info[i]:
                gap += i
            else:
                gap -= i

        if max_gap < gap:
            max_gap = gap
            lion_info.reverse()
            answer = lion_info

    return answer


solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0])
