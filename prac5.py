def solution(n):
    nums = sorted(str(int(n)),reverse=True)
    return int(''.join(nums))