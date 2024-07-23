# 볼링공 고르기

N, M = map(int, input().split()) # 볼링공 개수 N , 볼링공 무게 최댓값 M
K_list = list(map(int, input().split())) # 볼링공 무게 리스트

# 무게 별로 갯수 카운트
counting_list = []  
for k in set(K_list):
    counting_list.append(K_list.count(k))

# 경우의 수 다 계산
result = 0 
for i in range(len(counting_list)):
    for j in range(i+1, len(counting_list)):
      result += counting_list[i]*counting_list[j]

print(result)