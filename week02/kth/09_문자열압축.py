import sys
sys.stdin = open("09_문자열압축.txt", "r")

# 문제 분석
# 직관적으로는 완전 탐색으로 풀이할 수 있겠다.
# 1...S // 2의 크기로 슬라이싱을 한다. 
# S // 2 + 1의 크기의 경우 S 내에서 반복해서 나타날 수 없기에 1과 같다.
# xabcabcabc의 경우에는 어떻게 해도 압축을 할 수 없다. 반드시 0번 인덱스부터 차례로 압축해야 하므로.

# 접근
# 첫 번째 for문은 슬라이싱의 크기를 정한다. for i in range(S // 2 + 1)
    # 두 번째 while문은 배열의 끝에 도달할 때까지, 배열의 슬라이싱을 진행한다.
        # 현재 슬라이싱한 문자열이 '바로 이전의 문자열'과 동일한 경우 cnt += 1
        # 다른 경우 stack에 cnt push(), '바로 이전의 문자열' push(), cnt = 1
    # while문이 종료되면, stack을 문자열로 변경하고, 그것의 길이를 이전 최단 길이와 비교한다.
# 최단 길이를 return 한다.


def solution(S):
    answer = len(S)
    for block in range(1, len(S) // 2 + 1):

        stack = []
        prev_str = S[:block]
        cnt = 1

        for i in range(block, len(S) + 1, block):
            cur_str = S[i : i + block]

            if prev_str == cur_str: # 기존 값을 만났을 때
                cnt += 1

            elif prev_str != cur_str: # 새로운 값을 넣을 때
                if cnt >= 2:
                    stack.append(str(cnt))
                stack.append(prev_str)

                prev_str = cur_str
                cnt = 1
        else:
            stack.append(S[i:])

        tmp_completed_str = "".join(stack)
        answer = min(answer, len(tmp_completed_str))

    return answer