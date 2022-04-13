def solution(id_list, report, k):

    reprot_set = set(report)

    reportedList = {string:0 for string in id_list}
    ansL = {string:0 for string in id_list}
    banList = []

    for i in reprot_set:
        reportedList[i.split()[1]] += 1

    for i in id_list:
        if reportedList[i] > k-1:  
            banList.append(i)

    for i in reprot_set:
        if i.split()[1] in banList:
            ansL[i.split()[0]] += 1

    
    answer = list(ansL.values())
    return answer