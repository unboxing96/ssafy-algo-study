data = input()
list_data = list(data)
num_data = [] # 숫자만 들어갈 리스트데이터
eng_data = [] # 알파벳만 들어갈 리스트데이터

for i in list_data:
    try:
        num_data.append(int(i))
    except ValueError:
        eng_data.append(i)

# sort를 쓰면 정렬이 되지만 버블정렬로.
# num_data.sort()
# eng_data.sort()
def bubble_sort_data(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

bubble_sort_data(eng_data)
bubble_sort_data(num_data)

# 정렬한 데이터들을 알파벳부터 순서대로 빈 문자열 result에 삽입한 후 출력
result = ''
for i in eng_data:
    result += i

for j in num_data:
    result += str(j)
print(result)