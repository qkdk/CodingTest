from collections import Counter


def solution(want, number, discount):
    answer = 0
    want_dic = {}
    for i in range(len(want)):
        want_dic[want[i]] = number[i]

    want_dic = Counter(want_dic)

    for i in range(len(discount) - 9):
        tmp_list = discount[i: i + 10]
        if len(want_dic - Counter(tmp_list)) == 0:
            answer += 1
    return answer


solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1],
         ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana",
          "apple", "banana"])
