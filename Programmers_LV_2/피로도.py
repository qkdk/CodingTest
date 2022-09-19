from itertools import permutations


def solution(k, dungeons):
    per_list = list(permutations(dungeons, len(dungeons)))

    answer = -1

    for i in per_list:
        initial_k = k
        count = 0
        for j in range(len(dungeons)):
            if initial_k >= i[j][0]:
                initial_k -= i[j][1]
                count += 1
            else:
                break
        if answer < count:
            answer = count

    return answer


solution(80, [[80, 20], [50, 40], [30, 10]])
