def solution(s, n):
    answer = ''
    lowcast = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    upcast = [chr(x) for x in range(ord('A'), ord('Z') + 1)]

    for i in range(len(s)):
        if s[i] in lowcast:
            new_index = (lowcast.index(s[i]) + n)%26
            answer += lowcast[new_index]
        elif s[i] in upcast:
            new_index = (upcast.index(s[i]) + n)%26
            answer += upcast[new_index]
        else:
            answer+= ' '
    return answer

#파이썬 ord 함수는 문자를 숫자로 바꾸어준다.
#파이썬 chr 함수는 숫자를 문자로 바꾸어준다.

solution('ab', 1)