# a, b의 크기와 상관없이 입력 가능
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
