def solution(s):
    answer = ''
    s = [int(x) for x in s.split()]
    answer += str(min(s)) + ' ' + str(max(s))
    return answer


solution("1 2 3 4")
