n = int(input())
fear = list(map(int, input().split()))

fear.sort(reverse=True) # 오름차순 정렬
result = 0

while(fear!=[]): # 공포도 리스트가 빌 때 까지
    maxTemp = fear[0] # 리스트의 첫 번째 공포도가 현재 공포도 최댓값
    for i in range(maxTemp): 
        del fear[0] # 현재 공포도 최댓값 수로 한 그룹 구성(그룹에 한 명 배정될때마다 리스트 요소 비우기)
    result += 1 # 그룹 하나 생성

print(result)
