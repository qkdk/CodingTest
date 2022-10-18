from collections import defaultdict


def solution(genres, plays):
    answer = []
    genre_dic = defaultdict(list)
    count_dic = defaultdict(int)

    for i in range(len(plays)):
        genre_dic[genres[i]].append((i, plays[i]))
        count_dic[genres[i]] += plays[i]

    tmp = sorted(count_dic.items(), key=lambda x: -x[1])
    count_dic = dict(tmp)
    for key, value in genre_dic.items():
        tmp = sorted(value, key=lambda x: (-x[1], x[0]))
        genre_dic[key] = tmp

    for key in count_dic:
        tmp = 0
        for value in genre_dic[key]:
            if tmp == 2:
                break
            answer.append(value[0])
            tmp += 1

    print(genre_dic)
    print(count_dic)
    return answer


solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
