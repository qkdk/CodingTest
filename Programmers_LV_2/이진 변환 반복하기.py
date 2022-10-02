def solution(s):
    answer = []
    zero_count = 0
    count = 0

    # 1만 될때까지 반복하는 while
    while s != '1':
        # 0을 제거하는 반복문
        tmp = ''
        for i in s:
            if i == '1':
                tmp += '1'
            else:
                zero_count += 1
        s = tmp
        # 길이를 이진법으로 바꾸어주는 함수
        s = bin(len(s))
        s = s[2:]
        count += 1

    answer.append(count)
    answer.append(zero_count)
    return answer


solution("110010101001")
