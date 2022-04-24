

def solution(phone_book):
    answer = True
    phone_book.sort()
    print(phone_book)
    for num in range(len(phone_book)):
        for n in range(num+1, len(phone_book)):
            print(phone_book[n][:len(str(num))])
            if phone_book[n][:len(str(num))] == num:
                answer = False
                return answer
    return answer

phone_book = ["934793", "34", "44", "9347"]
print(solution(phone_book))