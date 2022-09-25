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


def solution(files):
    answer = []
    
    for file in files:
        answer.append(check_file(file))
        
    print(answer)
    return answer


files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))

files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
print(solution(files))