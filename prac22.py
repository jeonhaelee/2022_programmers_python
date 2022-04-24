
# def solution(phone_book):
#     answer = True
#     phone_book.sort()
#     phone_book = str(phone_book)
#     for i in range(len(phone_book)-1):
#         if phone_book[i+1].startswith(phone_book[i]):
#             answer = False
#             return answer
#     return answer

def solution(phone_book):
    answer = True
    phone_book.sort()
    phone_book = str(phone_book)
    for i in range(len(phone_book)-1):
        if phone_book[i+1:].startswith(phone_book[i]):
            answer = False
            return answer
    return answer

phone_book = ["934793", "34", "44", "9347"]
print(solution(phone_book))