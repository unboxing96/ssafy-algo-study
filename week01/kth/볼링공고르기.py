import sys
sys.stdin = open("볼링공고르기.txt", "r")

# 문제 분석
# 서로 무게가 다른 볼링공 고르기
# 같은 무게의 공이 여러 개 있더라도 서로 다른 공으로 간주

# 접근
# 완탐인가? 맞는 듯. 이걸 그리디라고 할 수 있나? 할 수 있는 듯.
# 각 무게마다, 더 무거운 무게의 종류 수를 모두 더해준다.

# 1 2 2 3 3
# 1: 4 * 1
# 2: 2 * 2
# 3: 0

# 1 2 2 3 4 4 5 5
# 1: 7 * 1
# 2: 5 * 2
# 3: 4 * 1
# 4: 2 * 2
# 5: 0

# # 완전 탐색 O(N ** 2) -> 정렬하고, 매 탐색마다 현재 무게보다 무거운 공의 수를 더 해준다.
# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# tot = 0

# arr.sort()

# for i in range(len(arr)):
#     tmp = 0
#     for j in range(i, len(arr)):
#         if arr[j] > arr[i]:
#             tmp += 1
#     tot += tmp

# print(tot)


# 그리디 O(N)

# Counter를 생성한다.
# 전체 value의 합 total을 구한다.
# 첫 번째 key에 대하여, total에서 현재 값을 빼고 남은 값 * 현재값을 result에 더한다.
# 이후 반복한다.
# 문제가 된다. 딕셔너리는 순서가 없기 때문에. 공의 무게를 인덱스로 하는 리스트로 바꾸자.

n, m = map(int, input().split())
arr = list(map(int, input().split()))
counter = [0] * (m + 1)
result = 0

arr.sort()

for elem in arr:
    # counter 배열의 인덱스 == 인덱스 무게의 공
    # counter 배열의 인덱스의 값 == 인덱스 무게의 공의 개수
    counter[elem] += 1

tot = sum(counter)

for idx in range(1, len(counter)):
    tot -= counter[idx]
    result += (tot * counter[idx])

print(result)