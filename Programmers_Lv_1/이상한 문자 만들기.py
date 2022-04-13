def solution(s):
    answer = ''

    flag = -1

    for i in range(len(s)):
        if s[i] == ' ':
            flag = -1
            answer += ' '
        elif flag == -1:
            answer += s[i].upper()
            flag = flag*-1
        else :
            answer += s[i].lower()
            flag = flag*-1
        
    return answer