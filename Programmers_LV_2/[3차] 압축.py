def solution(msg):
    answer = []
    dic = {}
    for i in range(1, 27):
        dic[chr(64 + i)] = i

    start_idx = 0
    end_idx = 0

    while True:
        end_idx += 1
        if end_idx > len(msg):
            answer.append(dic[msg[start_idx: end_idx]])
            break

        if msg[start_idx: end_idx + 1] not in dic:
            dic[msg[start_idx:end_idx + 1]] = len(dic) + 1
            answer.append(dic[msg[start_idx: end_idx]])
            start_idx = end_idx

    return answer


solution("KAKAO")
