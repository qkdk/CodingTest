from collections import deque


def solution(begin, target, words):
    q = deque()
    q.append([begin, 0])

    node = [0 for _ in range(len(words))]
    while q:
        word, count = q.popleft()

        if count > len(words):
            return 0

        if word == target:
            return count

        for index, tmp_word in enumerate(words):
            tmp_count = 0
            if node[index] == 1:
                continue
            for j in range(len(tmp_word)):
                if tmp_word[j] != word[j]:
                    tmp_count += 1
            if tmp_count == 1:
                q.append([tmp_word, count + 1])
                node[index] = 1

    return 0


solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
