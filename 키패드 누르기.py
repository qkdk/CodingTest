def solution(numbers, hand):
    answer =''

    lfing = '*'
    rfing = '#'

    for num in numbers:

        if num in [1,4,7]:
            answer += 'L'
            lfing = num

        elif num in [3,6,9]:
            answer += 'R'
            rfing = num

        else:
            keypad = {1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2],0:[3,1],'*':[3,0],'#':[3,2]}
            ldistance = abs(keypad[num][0] - keypad[lfing][0]) + abs(keypad[num][1] - keypad[lfing][1])
            rdistance = abs(keypad[num][0] - keypad[rfing][0]) + abs(keypad[num][1] - keypad[rfing][1])
    
            if ldistance > rdistance:
                rfing = num
                answer += 'R'
            elif rdistance > ldistance:
                lfing = num
                answer += 'L'
            else:
                if hand == 'right':
                    rfing = num
                    answer += 'R'
                else:
                    lfing = num
                    answer += 'L'

    return answer