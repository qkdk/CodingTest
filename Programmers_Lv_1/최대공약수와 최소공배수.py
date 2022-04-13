def solution(n, m):
    a = n
    b = m
    c = a%b
    while True:
        if c == 0:
            break
        else:
            a = b
            b = c
            c = a%b
    
    return [b,n*m/b]

solution(2,5)