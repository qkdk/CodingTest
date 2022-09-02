def solution(s):
    answer = int(1e9)

    for i in range(1, len(s) + 1):
        temp_string = s[0:i]
        count = 1
        for j in range(i, len(s), i):
            if temp_string[- i:] == s[j: j + i]:
                count += 1
            else:
                if count != 1:
                    temp_string = temp_string[:-i] + str(count) + temp_string[-i:] + s[j:j + i]
                    count = 1
                else:
                    temp_string = temp_string[:- i] + temp_string[- i:] + s[j:j + i]
                    count = 1
        if count != 1:
            temp_string = temp_string[:-i] + str(count) + temp_string[-i:]

        # print(i, temp_string)

        answer = min(answer, len(temp_string))

    # print(answer)
    return answer

# solution("a")
