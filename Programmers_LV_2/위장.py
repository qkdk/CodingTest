from collections import defaultdict


def solution(clothes):
    hash_map = defaultdict(list)

    for clothe in clothes:
        hash_map[clothe[1]].append(clothe[0])

    sum = 1
    for i in hash_map.values():
        sum *= len(i) + 1

    sum -= 1
    print(sum)
    return sum


solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
