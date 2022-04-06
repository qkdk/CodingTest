def solution(s):
    answer = ''
    ss = list(s)
    ss.sort()

    for i in range(1,len(ss)+1):
        answer += ss[-i]
    return answer

#sorted는 문자열도 정렬 가능
#join에 reverse 조건 달기 가능