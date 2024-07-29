import sys

sys.stdin = open('input.txt')

#  상하좌우:
# 입력값에 따른 이동으로 최종 위치 출력.
# 생각: R은 j의값이 +1 L은 -1 u는 i의값 -1 d는 i값 +1과 같이 이동 생각.
# 즉 2번째 입력값 i,j 플러스 마이너스 생각해주면됨.

# input 1번째 값
matrix_size = int(input())


i = 1
j = 1

# input된 리스트 체크 
input_list = list(map(str, input().split()))


# walk 와 U,D,R,L 에 따라 i,j값 변동
for walk in input_list:
    
    if walk == 'D' :
        if i == matrix_size:
            continue
        i += 1
    elif walk == 'U' :
        if i == 1:
            continue
        i -= 1

    elif walk == 'R' :
        if j >= matrix_size:
            continue
        j += 1
    elif walk == 'L' :
        if j <= 1 :
            continue
        j -= 1

print (i,j)
        

# 생각해본것.
# input만큼의 2차원 배열생성 필요없음
# matrix = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]                                                                                                                                                                                                                                                                                                                                                                                                                                                