

# def solution(prices):
#     answer = []
#     for i in range(len(prices)):
#         if i == len(prices)-1 :
#             answer.append(0)
#         for j in range(i+1, len(prices)):
#             if prices[i] > prices[j]:
#                 answer.append(j-i)
#                 j = len(prices)
#     return answer


def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        count = 0
        while prices[i] <= prices[i+1] :
            count += 1
        answer.append(count)
    answer.append(0)
    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))