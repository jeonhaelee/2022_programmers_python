# 파일명 정렬


def check_file(file):
    head = ""; number = ""; tail = ""
    for w in file:
        if w.isdigit():
            number += w
        else:
            if number != "":
                tail += w
            else:
                head += w
    result = [head, number, tail]
    return result


def head_sort(answer):
    
    head_li = []
    for head, number, tail in answer:
        if head.lower() not in head_li:
            head_li.append(head.lower())
    
    head_li.sort()
    
    result = []
    for target in head_li:
        for head, number, tail in answer:
            if head.lower() == target:
                result.append([head, number, tail])
    
    return result
    
    
def number_sort(answer):
    result = []
    return result


def tail_sort(answer):
    result = []
    return result


def solution(files):
    answer = []
    
    # head, number, tail 별로 구분지어 담아주기
    for file in files:
        answer.append(check_file(file))
        
    # 정렬하기
    ## head 정렬
    answer = head_sort(answer)
    
    ## number 정렬
    answer = number_sort(answer)
    
    ## tail 정렬 (위 조건이 다 같다면 입력 순으로)
    answer = tail_sort(answer)
    
    return answer


files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))

# files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
# print(solution(files))