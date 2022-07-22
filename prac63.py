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
    
    return answer

str1 = 'FRANCE'
str2 = 'french'
print(solution(str1, str2)) # 16384