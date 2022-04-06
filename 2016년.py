def solution(a, b):
    dow = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    s = sum(month[:a -1]) + b
    answer = dow[s%7]
    
    return answer

solution(5,24)