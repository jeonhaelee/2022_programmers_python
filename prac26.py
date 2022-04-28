
def f(i, prices):
    count = 0
    for j in range(i+1, len(prices)):
        print("prices[i] : {}, prices[j] : {}".format(prices[i], prices[j]))
        if prices[i] <= prices[j]:
            count += 1
        else: 
            count += 1
            break
    return count
            
def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        sub_answer = f(i, prices)
        answer.append(sub_answer)
        print("{}번째 후 answer : {}".format(i+1, answer))
    answer.append(0)
    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))