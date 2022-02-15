def solution(participant, completion):

    participant.sort()
    completion.sort()
    answer = participant[-1]

    for i in range(len(completion)):
        if completion[i] == participant[i]:
            pass
        elif completion[i] == participant[i+1]:
            answer = participant[i]
            return answer
    return answer


# import collections


# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]
# collection 모듈의 counter 는 리스트 객채의 개수를 dic형태로 반환해준다.


# def solution(participant, completion):
#     answer = ''
#     temp = 0
#     dic = {}
#     for part in participant:
#         dic[hash(part)] = part
#         temp += int(hash(part))
#     for com in completion:
#         temp -= hash(com)
#     answer = dic[temp]

#     return answer
# 해쉬값을 +-로 빈 해쉬값 찾음


# 원소의 Insert, Delete, Find ... <- Dic의 효율이 list 보다 좋음(다른 언어에서는 Hash Table)