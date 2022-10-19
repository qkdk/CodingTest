def solution(gems):
    answer = [0, len(gems) - 1]
    kind = len(set(gems))
    start, end = 0, 0
    gems_dic = {gems[0]: 1}

    while end < len(gems) and start < len(gems):
        if len(gems_dic) < kind:
            end += 1
            if end >= len(gems):
                break
            # gems_dic에 gem의 종류가 있는 경우
            if gems[end] in gems_dic:
                gems_dic[gems[end]] = gems_dic[gems[end]] + 1
            # gems_dic에 gem의 종류가 없는 경우
            else:
                gems_dic[gems[end]] = 1


        else:
            if gems_dic[gems[start]] > 1:
                gems_dic[gems[start]] = gems_dic[gems[start]] - 1
            else:
                del gems_dic[gems[start]]

            # 최소길이 업데이트
            if answer[1] - answer[0] > end - start:
                answer = [start, end]

            start += 1

    answer[0] = answer[0] + 1
    answer[1] = answer[1] + 1
    return answer


# solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
# solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])
solution(["A", "A", "B"])
