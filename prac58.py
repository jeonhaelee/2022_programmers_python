# 메뉴 리뉴얼
# 동 길이일 때는 가장 많이 나온 것을 채택. 동 길이가 여러개일 경우 여러개 다 채택.
# 나에게 남은 미션 : make_menu 함수 만들기.
from itertools import combinations

answer = []
count_answer = []
    
def make_menu(orders, n): # course에 해당하는 개수가 없을 때 임의로 만들기 위해 확인

    result = []
    
    menus = []
    for order in orders:
        if len(order) < n:
            continue
        order = list(order)
        menus.extend(list(combinations(order, n)))

    for menu in menus:
        result.append(''.join(menu))
        
    return result



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
    
    real_answer = []
    
    global answer
    global count_answer
    orders.sort(key = lambda x : len(x))
    
    make_course = []
    for co in course:
        co_count = 0
        for order in orders:
            if len(order) == co:
                co_count += 1
        if co_count > 1:
            make_course.append(co)
    
    
    for co in make_course:
        result = make_menu(orders, co)
        for r in result:
            if r in answer:
                count_answer[answer.index(r)] += 1
                continue
            answer.append(r)
            count_answer.append(1)
            
    print(f'orders : {orders}')
    
    # for i, order in enumerate(orders):
        
    #     if order in answer:
    #         count_answer[answer.index(order)] += 1
    #         continue
            
    #     if len(orders[i]) not in course:
    #         continue

    #     if compare_menu(i, orders):
    #         answer.append(orders)
    #         count_answer.append(1)

    print(f'answer : {answer}')
    print(f'count_answer : {count_answer}')
    
    # 동 길이일 때는 가장 많이 나온 것을 채택. 동 길이가 여러개일 경우 여러개 다 채택.
    
    for co in course:
        max = 2
        get = []
        for ans in answer:
            if len(ans) != co:
                continue
            if count_answer[answer.index(ans)] == max:
                get.append(ans)
            elif count_answer[answer.index(ans)] > max:
                max = count_answer[answer.index(ans)]
                get = [ans]
        real_answer.extend(get)

        
        
    return real_answer

# orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# course = [2,3,4]
# print(solution(orders, course)) # ["AC", "ACDE", "BCFG", "CDE"]

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]
print(solution(orders, course)) # ["ACD", "AD", "ADE", "CD", "XYZ"]

# orders = ["XYZ", "XWY", "WXA"]
# course = [2,3,4]
# print(solution(orders, course)) # ["WX", "XY"]
