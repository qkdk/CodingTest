from itertools import permutations
from collections import deque


def solution(expression):
    operation = ['*', '+', '-']
    tmp_operation = set([])

    q1 = deque()
    lst1 = []
    lst2 = []
    answers = []

    tmp = ''
    for exp in expression:
        if exp in operation:
            lst1.append(int(tmp))
            lst1.append(exp)
            tmp_operation.add(exp)
            tmp = ''
        else:
            tmp += exp
    lst1.append(int(tmp))

    operations = list(permutations(tmp_operation, len(tmp_operation)))

    for oper in operations:
        q1 = deque(lst1)
        for op in oper:
            while q1:
                if q1[0] == op:
                    tmp = calculate(lst2[-1], q1[1], op)
                    lst2.pop()
                    q1.popleft()
                    q1.popleft()
                    lst2.append(tmp)
                    continue

                lst2.append(q1[0])
                q1.popleft()

            q1 = deque(lst2)
            lst2.clear()

        answers.append(abs(q1[0]))

    return max(answers)


def calculate(num1, num2, oper):
    if oper == '*':
        return num1 * num2
    elif oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2


solution("100-200*300-500+20")
