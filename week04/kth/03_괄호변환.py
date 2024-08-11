# 문제 분석
# 앞에서부터 차례로 읽어 '균형잡힌 괄호'가 되면 분리하는 함수 separate
# 분리한 앞 문자열 u가 '올바른 괄호'라면 v에 대해 separate 수행
    # 수행 결과 u에 붙인 후 return
# 아니라면
    # 일련의 동작

def separate(w):
    open_count = 0
    close_count = 0
    for idx, elem in enumerate(w):
        if elem == "(":
            open_count += 1
        else:
            close_count += 1
        
        if open_count == close_count:
            return w[:idx+1], w[idx+1:]

def perfection_check(u):
    stack = []
    for elem in u:
        if elem == "(":
            stack.append(elem)
        elif elem == ")":
            if not stack:
                return False
            stack.pop()
    return not stack

def make_perfection(u, v):
    tmp = "("
    tmp += solution(v)
    tmp += ")"
    for s in u[1:len(u)-1]:
        if s == '(':
            tmp += ')'
        else:
            tmp += '('
    return tmp

def solution(p):
    if len(p) == 0:
        return ""

    u, v = separate(p)

    if perfection_check(u):
        return u + solution(v)
    else:
        return make_perfection(u, v)

p = "()))((()"
result = solution(p)
print(result)
