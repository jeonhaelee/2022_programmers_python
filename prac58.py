# 메뉴 리뉴얼

def make_menu():# course에 해당하는 개수가 없을 때 임의로 만들기 위해 확인
    return ""

def compare_menu(i, orders): # course에 해당하는 개수가 있을 때 확인
    target = list(orders[i])
    
    result = False
    for j in range(i+1, len(orders)):
        compare_target = list(orders[j])
        for t in target:
            if t not in compare_target:
                break
        result = True
        
    return result

def solution(orders, course):
    answer = []
    orders.sort(key = lambda x : len(x))
    
    print(f'orders : {orders}')
    
    for i, order in enumerate(orders):
        if compare_menu(i, orders):
            answer.append(orders[i])

    return answer

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
print(solution(orders, course)) # ["AC", "ACDE", "BCFG", "CDE"]

