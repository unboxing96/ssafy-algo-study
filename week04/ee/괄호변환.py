# 괄호 변환
def right(chars):
    status = 0
    for char in chars:
        if char == "(":
            status += 1
        else:
            status -= 1
        if status < 0:  # 음수가 되는 순간이 있다면 올바른 괄호 문자열이 아님 (짝이 맞지 않음)
            return False
    return True


def separate(chars): # 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
    u, v = '', ''
    status = 0
    for idx in range(len(chars)):
        if chars[idx] == "(":
            status += 1
        elif chars[idx] == ")":
            status -= 1
        if status == 0:
            u = chars[:idx + 1]
            v = chars[idx + 1:]
            return u, v

def solution(chars):
    if not chars: # 입력이 빈 문자열이라면
        return chars # 빈 문자열 그대로 반환
    u, v = separate(chars) # 균헝잡힌 문자열 u,v로 분리
    if right(u): # u가 올바른 문자열이라면
        return u + solution(v)
    else: # u가 올바른 문자열이 아니라면
        # return "(" + solution(v) + ")" + u[-2:0:-1] 이건 왜 안 될까?
        temp = ''
        for s in u[1:-1]:
            if s == '(':
                temp += ')'
            else:
                temp += '('
        return "(" + solution(v) + ")" + temp
        