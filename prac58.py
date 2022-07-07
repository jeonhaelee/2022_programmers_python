# 메뉴 리뉴얼
# 동 길이일 때는 가장 많이 나온 것을 채택. 동 길이가 여러개일 경우 여러개 다 채택.
# 나에게 남은 미션 : make_menu 함수 만들기.

def make_menu(orders, course): # course에 해당하는 개수가 없을 때 임의로 만들기 위해 확인
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
    sub_answer = []
    orders.sort(key = lambda x : len(x))
    
    make_menu()
    
    print(f'orders : {orders}')
    
    for i, order in enumerate(orders):
        
        if order in answer:
            sub_answer[answer.index(order)] += 1
            continue
            
        if len(orders[i]) not in course:
            continue

        if compare_menu(i, orders):
            answer.append(orders)
            sub_answer.append(1)


    # 동 길이일 때는 가장 많이 나온 것을 채택. 동 길이가 여러개일 경우 여러개 다 채택.
    
    return answer

# orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# course = [2,3,4]
# print(solution(orders, course)) # ["AC", "ACDE", "BCFG", "CDE"]

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]
print(solution(orders, course)) # ["ACD", "AD", "ADE", "CD", "XYZ"]

# orders = ["XYZ", "XWY", "WXA"]
# course = [2,3,4]
# print(solution(orders, course)) # ["WX", "XY"]
