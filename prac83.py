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
    
    print(f'head_li : {head_li}')
    
    
    
    
def solution(files):
    answer = []
    
    # head, number, tail 별로 구분지어 담아주기
    for file in files:
        answer.append(check_file(file))
        
    # 정렬하기
    ## head 정렬, number 정렬, 그래도 같다면 tail은 입력 순으로
    head_sort(answer)
    
    
    return answer


files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))

# files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
# print(solution(files))