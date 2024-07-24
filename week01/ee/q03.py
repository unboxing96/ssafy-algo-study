# 문자열 뒤집기

nums = input()
count = 0
for i in range(len(nums)-1):
    if nums[i]!=nums[i+1]:
        count += 1
print(int(count/2+0.5))