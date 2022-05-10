
def solution(s):
    answer = [] # answer의 크기는 len(s)
    d = []; sub = []; num = ""
    for i in range(1, len(s)-1):
        if s[i] == "{":
            sub = []
        if s[i].isdigit():
            num += s[i]
        if s[i] == ",":
            if s[i+1] == "{":
                continue
            sub.append(int(num))
            num = ""
        if s[i] == "}":
            sub.append(int(num))
            num = ""
            d.append(sub)
            if s[i+1] == "}":
                break
    d.sort(key=len) # d 리스트 안의 sub 리스트 길이순으로 정렬하기
    for nums in d:
        for num in nums:
            if num not in answer:
                answer.append(num)
    return answer
