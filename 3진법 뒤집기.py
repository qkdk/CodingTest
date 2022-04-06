def solution(n):
    answer = 0

    conv = []
    while (n >= 3):
        conv.append(n%3)
        n = n//3
    conv.append(n)
    
    for i in range(len(conv)):
        answer += 3**i * conv[-(i+1)]

    return answer

solution(45)