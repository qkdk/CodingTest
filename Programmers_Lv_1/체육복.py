def solution(n, lost, reserve):
    s_reserve = set(reserve) - set(lost)
    s_lost = set(lost) - set(reserve)

    for i in s_lost:
        if i - 1 in s_reserve:
            s_reserve.remove(i-1)
            n += 1
        elif i+1 in s_reserve:
            s_reserve.remove(i+1)
            n += 1

    answer = n - len(s_lost)
    return answer


solution(5, [2, 4], [1, 3, 5])
