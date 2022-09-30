from itertools import combinations
from collections import Counter


def solution(relation):
    cols = len(relation[0])
    lst_index = []
    combis = []

    for i in range(cols):
        lst_index.append(i)

    for i in range(1, cols + 1):
        combis.extend(list(combinations(lst_index, i)))

    uniques = []

    for indexes in combis:
        # 검사해서 최소성을 만족하는 combis 만 계산
        if not check_mini(indexes, uniques):
            continue
        if check_unique(relation, indexes):
            uniques.append(indexes)

    answer = len(uniques)
    return answer


def check_mini(indexes, uniques):
    for i in uniques:
        inter = set(i) & set(indexes)
        if inter and len(inter) == len(i):
            return False
    return True


def check_unique(relations, indexes):
    # 필요한것들만 배열 만들기
    tmp_list = []
    for i in range(len(relations)):
        tmp_str = ""
        for index in indexes:
            tmp_str += relations[i][index]
        tmp_list.append(tmp_str)

    for i in Counter(tmp_list).values():
        if i != 1:
            return False

    return True


#
# solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
#           ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]])

# solution([['a', 'b', 'c'],
#           ['1', 'b', 'c'],
#           ['a', 'b', '4'],
#           ['a', '5', 'c']
#           ])

solution([['a', '1', '4'],
          ['2', '1', '5'],
          ['a', '2', '4']
          ])
