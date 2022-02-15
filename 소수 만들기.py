def solution(nums):

    answer = 0
    answerList = []

    for i in range(len(nums) - 2):
        for j in range(i+1, len(nums) - 1):
            for k in range(j+1, len(nums)):
                answerList.append(nums[i] + nums[j] + nums[k])
            
    for i in answerList:
        flag = 0
        for j in range(2, i-1):
            if i%j == 0:
                flag = 1

        if flag == 0:
            answer += 1

    return answer
