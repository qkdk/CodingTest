# from collections import deque
#
#
# def solution(info, query):
#     ori_info = []
#     ori_query = []
#     answers = []
#
#     for i in info:
#         ori_info.append(i.split())
#
#     for i in query:
#         ori_query.append([x for x in i.split() if x != 'and'])
#
#     q_query = deque(ori_query)
#
#     while q_query:
#         tmp_info = ori_info[::]
#         tmp_info2 = []
#         cur_query = q_query[0]
#
#         for cur_index in range(len(cur_query) - 1):
#             if cur_query[cur_index] == '-':
#                 continue
#             for info in tmp_info:
#                 if cur_query[cur_index] == info[cur_index]:
#                     tmp_info2.append(info)
#
#             tmp_info = tmp_info2[::]
#             tmp_info2.clear()
#
#         for i in tmp_info:
#             if int(cur_query[-1]) <= int(i[-1]):
#                 tmp_info2.append(i)
#         tmp_info = tmp_info2[::]
#         tmp_info2.clear()
#
#         answers.append(len(tmp_info))
#         q_query.popleft()
#
#     return answers

from itertools import combinations
from collections import defaultdict
from bisect import bisect_left, bisect_right


def solution(infos, queries):
    answer = []
    hashmap = defaultdict(list)
    for i in infos:
        # 하나의 인포
        info = i.split()
        keys = info[:4]
        score = int(info[4])

        for j in range(5):
            # 하나의 인포, - 가 붙을수 있는 상황 0~4
            indexes = list(combinations([0, 1, 2, 3], j))
            # 리스트 여러개가 나옴
            for index in indexes:
                # 리스트 하나의 여러개의 index값
                tmp = keys.copy()
                for idx in index:
                    tmp[idx] = '-'
                hashmap[tuple(tmp)].append(score)

    # print(hashmap)

    # 파이썬 딕셔너리 정렬방법
    for i in hashmap.values():
        i.sort()

    # print('\n')
    # print(hashmap)

    for query in queries:
        # 하나의 쿼리
        query_count = 0
        query = query.replace("and ", "")
        query = query.split()
        query_key = tuple(query[:4])
        query_score = int(query[4])

        if query_key in hashmap:
            key_list = hashmap[query_key]
            # query_count = bisect_right(key_list, query_score)
            idx = bisect_left(key_list, query_score)
            query_count = len(key_list) - idx

        answer.append(query_count)

    return answer


solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
          "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
         ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
          "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
          "- and - and - and - 150"])
