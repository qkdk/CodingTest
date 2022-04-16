def solution(w,h):

    # 영향을 받는 사각형의 수 공식 : W+H-1
    a = w
    b = h
    c = -1
    while True:
        c = a%b
        if c == 0:
            gcd = b
            break
        a = b
        b = c

    cutW = w/gcd
    cutH = h/gcd

    return w*h - gcd*(cutH + cutW -1)

solution(8,12)

# def gcd(a,b): return b if (a==0) else gcd(b%a,a) 
# 재귀함수를 이용한 gcd 구하기