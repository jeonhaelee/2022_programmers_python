# 뉴스 클러스터링

def solution(str1, str2):
    answer = 0
    str1_list = []; str2_list = []
    
    for i in range(len(str1)-1):
        str = str1[i:i+2]
        if str.isalpha() :
            str1_list.append(str.lower())
    
    for i in range(len(str2)-1):
        str = str2[i:i+2]
        if str.isalpha() :
            str2_list.append(str.lower())
    
    print(str1_list)
    print(str2_list)
    
    if len(str1_list) == 0 and len(str2_list) == 0:
        answer = 1
    
    li = str1_list
    li.extend(str2_list)
    li = set(li)
    
    print(f'li : {li}')
    
    sum_count = len(set(li))
    print(f'sum_count : {sum_count}')
    
    inter_count = 0
    for word in str1_list:
        if word in str2_list:
            inter_count += 1
            del str2_list[str2_list.index(word)]
    print(f'inter_count : {inter_count}')
    
    answer = int((inter_count/sum_count) * 65536)   
            
    return answer

str1 = 'FRANCE'
str2 = 'french'
print(solution(str1, str2)) # 16384