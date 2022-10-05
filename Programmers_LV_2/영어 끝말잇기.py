    def solution(n, words):
        dic = {}
        prev_char = ''

        for index, word in enumerate(words):
            if word in dic:
                count = index
                break

            elif prev_char != word[0] and prev_char != '':
                count = index
                break

            prev_char = word[-1]
            dic[word] = True

        else:
            return [0, 0]

        answer = [count % n + 1, count // n + 1]
        return answer


solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])
