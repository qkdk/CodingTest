def solution(price, money, count):
    pricesum = 0
    answer = -1

    for i in range(1,count+1):
        pricesum += i*price

    answer = pricesum - money

    if answer < 0 :
        answer = 0 

    return answer