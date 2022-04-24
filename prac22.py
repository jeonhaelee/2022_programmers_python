

def solution(phone_book):
    answer = True
    phone_book.sort()
    for num in range(len(phone_book)):
        set = phone_book[num]
        for n in range(num+1, len(phone_book)):
            number = str(phone_book[n])
            if number[:len(str(set))] == str(set):
                answer = False
                return answer
    return answer

phone_book = ["934793", "34", "44", "9347"]
print(solution(phone_book))