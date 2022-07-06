# 메뉴 리뉴얼

def compare_menu(i, orders):
    target = orders[i]
    
    for order in range(i+1, len(orders)):
        if order[:len(target)] == target:
            return True
        
def solution(orders, course):
    answer = []
    orders.sort(key = lambda x : len(x))
    
    for i, order in enumerate(orders):
        if compare_menu(i, orders):
            answer.append(orders[i])

    return answer

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
print(solution(orders, course)) # ["AC", "ACDE", "BCFG", "CDE"]