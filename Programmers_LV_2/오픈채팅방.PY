def solution(record):
    answer = []
    result = []
    accountDB = {}
    actionDB = {"Enter" : "님이 들어왔습니다.", "Leave" : "님이 나갔습니다."}

    #result엔 ID와 Action을 담고 나중에 맵핑
    #accountDB에 아이디별 최신 아이디 업데이트

    for i in record:
        temp = i.split()

        if temp[0] == "Enter":
            accountDB[temp[1]] = temp[2]
            result.append(temp[0])
            result.append(temp[1])

        elif temp[0] == "Leave":
            result.append(temp[0])
            result.append(temp[1])

        else:
            accountDB[temp[1]] = temp[2]


    for i in range(int(len(result)/2)):
        action = result[i*2]
        id = result[i*2+1]

        answer.append(accountDB[id] + actionDB[action])

    return answer