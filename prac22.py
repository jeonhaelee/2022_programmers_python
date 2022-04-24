

def solution(phone_book):
    answer = True
    head = phone_book[0]
    for number in range(1, len(phone_book)):
        if phone_book[number][:len(head)] == head:
            answer = False
            return answer
    return answer