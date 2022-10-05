def solution(s):
    answer = ''

    flag = True
    for i in s:
        if i == ' ':
            flag = True

        elif i.isdigit():
            flag = False

        else:
            if flag:
                i = i.upper()
            else:
                i = i.lower()
            flag = False

        answer += i

    return answer


solution("3people unFollowed me")
# solution("a aa ")
