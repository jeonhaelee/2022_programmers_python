

def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for num in range(len(phone_book)):
        for n in range(num+1, len(phone_book)):
            if phone_book[n][:len(num)] == num:
                answer = False
                return answer
    return answer

phone_book = ["934793", "34", "44", "9347"]
print(solution(phone_book))