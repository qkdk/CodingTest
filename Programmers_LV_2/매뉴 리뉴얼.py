from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []
    lst_dict = {}
    for i in course:
        lst_dict[i] = []

    for order in orders:
        for c in course:
            if len(order) >= c:
                tmp = []
                for i in list(combinations(order, c)):
                    tmp.append(''.join(sorted(i)))
                lst_dict[c].extend(tmp)

    for i in course:
        tmp_c = Counter(lst_dict[i])
        for key in tmp_c.keys():
            if max(tmp_c.values()) == tmp_c[key] and tmp_c[key] > 1:
                answer.append(key)

    answer.sort()
    return answer


# solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])
solution(["XYZ", "XWY", "WXA"], [2, 3, 4])
