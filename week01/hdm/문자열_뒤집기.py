import sys

sys.stdin = open('index.txt')

data = input()

count0 = 0
count1 = 0

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count0 +=1
        else:
            count1 +=1

print(min(count0,count1))


# zero_or_one = list(input())
# zero = zero_or_one.count('0') 
# one = zero_or_one.count('1')

# result = 0

# if zero > one :
#     for index, value in enumerate(zero_or_one):
#         if value == '1':
#             zero_or_one[index] = '0'
#             result += 1

        
# elif one < zero:
#     for index, value in enumerate(zero_or_one):
#         if value == '0':
#             zero_or_one[index] = '1'
#             result += 1

# print(result)