from collections import deque


def divide_string(v):
    balance_dic = {'(': 1, ')': -1}
    v = deque(v)
    tmp_list = []
    stack = []
    count = 0
    balance = 0

    while not (count > 0 and balance == 0):
        pop_item = v.popleft()
        tmp_list.append(pop_item)
        stack.append(pop_item)
        if stack[-2:] == ['(', ')']:
            stack.pop()
            stack.pop()

        balance += balance_dic[tmp_list[-1]]
        count += 1

    u = ''.join(tmp_list)
    v = ''.join(v)
    flag = False
    if not stack:
        flag = True

    return u, v, flag


def solution(p):
    reverse = {'(': ')', ')': '('}

    if not p:
        return p

    u, v, flag = divide_string(p)

    if flag:
        return u + solution(v)
    else:
        tmp = '(' + solution(v) + ')'
        for i in u[1:-1]:
            tmp = tmp + reverse[i]
        return tmp


solution("()))((()")
