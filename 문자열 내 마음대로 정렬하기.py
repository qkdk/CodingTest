def solution(strings, n):
    anli = []
    
    for i in strings:
        anli.append(i[n] + i)
    anli.sort()
    
    answer = [x[1:] for x in anli]

    return answer