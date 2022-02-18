def solution(answers):
    answer = []
    pattern = {0: [1, 2, 3, 4, 5], 1: [2, 1, 2, 3, 2,
                                       4, 2, 5], 2: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]}
    pattern2 = {0: [], 1: [], 2: []}
    ctCorrect = [0,0,0]

    for i in range(3):
        di = len(answers) / len(pattern[i])
        md = len(answers) % len(pattern[i])
        for j in range(int(di)):
            pattern2[i].extend(pattern[i])
        for k in range(md):
            pattern2[i].append(pattern[i][k])
        
    for i in range(3):
        for j in range(len(answers)):
            if answers[j] == pattern2[i][j]:
                ctCorrect[i] += 1
    
    m = max(ctCorrect)        
    answer = [x+1 for x,v in enumerate(ctCorrect) if v == m]

    return answer

solution([1,2,3,4,5])