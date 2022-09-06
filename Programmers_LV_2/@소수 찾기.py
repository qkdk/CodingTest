# 순열과 조합을 찾아주는 라이브러리
# input으로 리스트 iterable
from itertools import combinations, permutations
import math


def solution(numbers):
    answer = 0
    per_num = []
    for i in range(len(numbers)):
        per_num.extend(list(permutations(numbers, i + 1)))

    lst = []
    for i in per_num:
        tmp = ""
        for j in i:
            tmp += j
        tmp = int(tmp)
        if tmp == 1 or tmp == 0:
            continue
        lst.append(tmp)

    lst = set(lst)
    for i in lst:
        answer += is_prime_number(i)
    print(lst)
    print(answer)
    return answer


def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return 0
    return 1


# solution("17")
solution("011")
# solution("104194")
