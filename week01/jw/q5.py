# 볼링공의 개수 N, 공의 최대무게는 M

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort() # 오름차순 정렬

'''
data 내 숫자 개수 구하기
오름차순으로 정렬 후 숫자가 바뀔 때 result값이 추가되니
같은 숫자일 때는 추가되는 값이 같으므로 곱하려고 함
'''
count_dict = {}
for num in data:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

result = 0 # 최종 출력 값
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        result += (n-i-1)*count_dict[data[i]]

print(result)