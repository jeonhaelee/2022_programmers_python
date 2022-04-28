

def solution(prices):
    answer = []
    for i in range(len(prices)):
        if i == len(prices)-1 :
            answer.append(0)
        count = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                count += 1
        answer.append(count)
    return answer

prices = [1, 6, 5, 4, 0]
print(solution(prices))