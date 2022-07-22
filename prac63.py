# 뉴스 클러스터링

# 내 풀이
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
    
    total_len = len(str1_list) + len(str2_list)
    
    if len(str1_list) == 0 and len(str2_list) == 0:
        return 65536  
 
    inter_count = 0
    for a in str1_list:
        if a in str2_list:
            inter_count += 1
            del str2_list[str2_list.index(a)]

    sum_count = total_len - inter_count
    
    answer = int((inter_count/sum_count) * 65536)   
            
    return answer

# str1 = 'FRANCE'
# str2 = 'french'
# print(solution(str1, str2)) # 16384

# str1 = 'handshake'
# str2 = 'shake hands'
# print(solution(str1, str2)) # 65536

# str1 = 'E=M*C^2'
# str2 = 'e=m*c^2'
# print(solution(str1, str2)) # 65536

str1 = 'aa1+aa2'
str2 = 'AAAA12'
print(solution(str1, str2)) # 43690

# 다른 사람 풀이
import re
import math

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)