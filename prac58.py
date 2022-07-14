# 메뉴 리뉴얼
# 동 길이일 때는 가장 많이 나온 것을 채택. 동 길이가 여러개일 경우 여러개 다 채택.


from itertools import combinations


def make_menu(num, orders):

    result = []
    
    menu_list = []
    menu_count = []
    
    menu_sum = []
    for order in orders:
        order = list(order)
        menus = list(combinations(order,num))
        menu_sum.extend(menus)
    
    for menu in menu_sum:
        menu = list(menu)
        menu.sort()
        menu = ''.join(menu)

        if menu in menu_list:
            menu_count[menu_list.index(menu)] += 1
        else:
            menu_list.append(menu)
            menu_count.append(1)
        
    
    point = 2
    for i in range(len(menu_count)):
        if menu_count[i] < 2:
            continue
        elif menu_count[i] > point:
            point = menu_count[i]
    
    for i in range(len(menu_count)):
        if menu_count[i] == point:
            result.append(menu_list[i])

    return result

def solution(orders, course):

    answer = []
    
    for num in course:
        answer.extend(make_menu(num, orders))
    
    answer.sort()
    
    return answer


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
print(solution(orders, course)) # ["AC", "ACDE", "BCFG", "CDE"]

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]
print(solution(orders, course)) # ["ACD", "AD", "ADE", "CD", "XYZ"]

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
print(solution(orders, course)) # ["WX", "XY"]
