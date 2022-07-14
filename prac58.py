# 메뉴 리뉴얼
# 동 길이일 때는 가장 많이 나온 것을 채택. 동 길이가 여러개일 경우 여러개 다 채택.


from itertools import combinations

g_orders = []

def make_menu(num):
    global g_orders
    result = []
    
    menu_count = []
    
    for order in g_orders:
        order = list(order)
        menus = list(combinations(order,num))
        
    for menu in menus:
        menu = list(menu)
        menu.sort()
        menu = ''.join(menu)
        if menu in menu_count:
            menu_count[menu_count.index(menu)][1] += 1
        else:
            menu_count.append([menu, 1])
            
    point = 2
    for i in range(len(menu_count)):
        if menu_count[i][1] < 2:
            continue
        elif menu_count[i][1] > point:
            point = menu_count[i][1]
    
    for i in range(len(menu_count)):
        if menu_count[i][1] == point:
            result.append(menu_count[i][0])
    
    return result

def solution(orders, course):
    global g_orders
    g_orders = orders
    answer = []
    
    for num in course:
        answer.extend(make_menu(num))
        
    return answer.sort()


# orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# course = [2,3,4]
# print(solution(orders, course)) # ["AC", "ACDE", "BCFG", "CDE"]

# orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
# course = [2,3,5]
# print(solution(orders, course)) # ["ACD", "AD", "ADE", "CD", "XYZ"]

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
print(solution(orders, course)) # ["WX", "XY"]
