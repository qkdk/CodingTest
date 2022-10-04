from collections import deque


def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        skill_tree = deque(skill_tree)
        skill_q = deque(skill)
        while skill_tree:
            if skill_tree[0] in skill_q:
                if skill_tree[0] == skill_q[0]:
                    skill_tree.popleft()
                    skill_q.popleft()
                else:
                    break
            else:
                skill_tree.popleft()

            if len(skill_tree) == 0:
                answer += 1

    return answer


solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])
