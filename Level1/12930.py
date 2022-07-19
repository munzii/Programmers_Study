def solution(s):
    slist = s.split(' ')
    answer = ''
    for word in slist:
        for i, letter in enumerate(word):
            if i % 2 ==0:
                answer += letter.upper()
            else:
                answer += letter.lower()
        answer += ' '
    return answer[:-1]

print(solution("try hello world"))