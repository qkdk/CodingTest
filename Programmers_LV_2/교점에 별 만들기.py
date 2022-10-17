from itertools import combinations


def find_joint(list_a, list_b):
    A, B, E = list_a
    C, D, F = list_b

    try:
        result = ((B * F - E * D) / (A * D - B * C), (E * C - A * F) / (A * D - B * C))
    except:
        return (1001, 1001)

    return result


def solution(line):
    answer = []
    dic = {}
    for i in combinations(line, 2):
        x, y = find_joint(i[0], i[1])
        if x == 1001:
            continue
        if int(x) == x and int(y) == y:
            dic[(int(x), int(y))] = 1

    xs, ys = zip(*dic)
    x_max, y_max, x_min, y_min = max(xs), max(ys), min(xs), min(ys)

    print(x_min, x_max, y_min, y_max)
    for i in range(y_max, y_min - 1, -1):
        tmp = ''
        for j in range(x_min, x_max + 1):
            if (j, i) in dic:
                tmp += '*'
            else:
                tmp += '.'
        answer.append(tmp)

    return answer


#
# solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]])
# solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]])
# solution([[1, -1, 0], [2, -1, 0]])
solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]])
