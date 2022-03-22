def solution(n):
    nums = []
    answer = ""
    for i in range(len(str(n))):
        nums.append(int(str(n)[i]))
    nums.sort(reverse=True)
    for i in nums:
        answer += str(i)
    return int(answer)