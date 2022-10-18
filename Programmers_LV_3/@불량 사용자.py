from itertools import permutations


def check_id(id_str, ban_str):
    if len(id_str) != len(ban_str):
        return False

    for a, b in zip(id_str, ban_str):
        if b == '*':
            continue
        if a != b:
            return False

    return True


def solution(user_id, banned_id):
    answer = []

    for i in permutations(user_id, len(banned_id)):
        set_i = set(i)
        for a, b in zip(i, banned_id):
            if not check_id(a, b):
                break
        else:
            if set_i not in answer:
                answer.append(set_i)

    return len(answer)


# solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])
