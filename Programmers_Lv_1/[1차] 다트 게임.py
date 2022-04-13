def solution(dartResult):
    answer = 0
    dict1 = {'S':1, 'D':2, 'T':3}
    answerlist = []
    answerindex = -1
    tempcount = 0

    for i in range(len(dartResult)):
        tempcount += 1
        if dartResult[i] in dict1.keys():
            if tempcount == 3:
                answerlist.append(10**dict1[dartResult[i]])
            else:
                answerlist.append(int(dartResult[i-1])**dict1[dartResult[i]])
                answerindex += 1

            tempcount = 0
            
        elif dartResult[i] == '*':
            tempcount = 0
            answerlist[answerindex] = answerlist[answerindex]*2
            if answerindex > 0:
                answerlist[answerindex-1] = answerlist[answerindex-1]*2

        elif dartResult[i] == '#':
            tempcount = 0
            answerlist[answerindex] = answerlist[answerindex] * -1

    answer = sum(answerlist)
    return answer

solution("1D2S#10S")
