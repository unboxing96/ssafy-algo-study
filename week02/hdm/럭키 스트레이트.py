import sys
sys.stdin = open('input.txt')

# 럭키 스트레이트:
# 점수 N을 기준으로 반으로 나누었을때 왼쪽 오른쪽을 비교.
# 왼쪽 오른쪽의 값이 동일하면, LUCKY! 다르면 READY!

#LIST 슬라이싱을 활용해서 SUM함수를 통해 좌 우측값 비교하는것을 활용함.



#input.txt시에 요소들이 string으로 들어옴.
A = list(input())

# number을 int로 변환 리스트 컴프리핸션 활용!
number = [int(x) for x in A]

# 리스트 슬라이싱 
half = int(len(number) / 2)
compair1 = number[:half]
compair2 = number[half:]

# SUM 함수 활용
compair1_sum = sum(compair1)
compair2_sum = sum(compair2)

# SUM값 비교 후 출력.
if compair1_sum == compair2_sum : 
    print("LUCKY")
else: print("READY")

# 공부 내용
# == 동등연산자. 값 자체를 비교하기에 값이 같으면 TRUE 반환
# is 식별 연산자. 두 객체의 메모리 주소가 같은지 확인(같은 객체인지 확인)