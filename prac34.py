def solution(skill, skill_trees):
    answer = 0
    for words in skill_trees:
      result = ""
      for word in words:
        if word in skill:
          result += word
      if skill.startswith(result):
        answer += 1
    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))