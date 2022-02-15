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