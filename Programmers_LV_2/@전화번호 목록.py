# # 선형 탐색 사영 => 시간 초과
# def solution(phone_book):
#     for i in range(len(phone_book)):
#         length = len(phone_book[i])
#         for j in range(i + 1, len(phone_book)):
#             if phone_book[j][:length] == phone_book[i]:
#                 return False
#     return True

def solution(phone_book):
    hashMap = {}

    for i in range(len(phone_book)):
        hashMap[phone_book[i]] = i
    for i in range(len(phone_book)):
        temp = ''
        for j in phone_book[i]:
            temp += j
            if temp in hashMap and hashMap[temp] != i:
                return False

    return True


solution(["119", "97674223", "1195524421"])
solution(["123", "456", "789"])
solution(["12", "123", "1235", "567", "88"])
