# 문자열 압축

def solution(s):
    
    # 문자열 길이가 하나일 때는 그냥 하나입니다.
    # 이걸 생각하지 않아서 한참을 헤맸습니다
    # 아놔!!!!!!!!!!
    if len(s) == 1:
        return 1

    answer = 0
    compressed_len = [0]*(len(s)//2)

    # 압축하는 블럭의 사이즈는 1부터 len(s)/2 까지
    for size in range(1, len(s)//2 + 1):

        compressed_s = ""
        # 첫 번째 블럭 넣기
        previous_block = s[:size]
        count = 1

        # 두 번째 블럭부터 비교하기
        for i in range(size, len(s), size):
            block = s[i: i+size]

            # 이전 블럭과 현재 블럭이 같으면 count ++
            if previous_block == block:
                count += 1
            else:
                # 다른데 count값이 1보다 크면 숫자+블럭 포맷으로 압축문자열에 추가
                if count > 1:
                    compressed_s += str(count) + previous_block
                # 압축되지 않는 블럭은 그냥 추가
                else:
                    compressed_s += previous_block
                # count값 1로 초기화
                count = 1
            # 현재 블럭을 previous_block에 넣고 반복문 마무리
            previous_block = block

        # 마지막 블럭 처리
        if count > 1:
            compressed_s += str(count) + previous_block
        else:
            compressed_s += previous_block
        
        # 압축한 문자열의 길이를 리스트에 추가
        compressed_len[size-1] = len(compressed_s)

    # 최소 문자열 길이를 반환
    answer = min(compressed_len)
    return answer

print(solution("aabbaccc")) # 7
print(solution("ababcdcdababcdcd")) #9
print(solution("abcabcdede")) #8
print(solution("abcabcabcabcdededededede")) #14
print(solution("xababcdcdababcdcd")) #17