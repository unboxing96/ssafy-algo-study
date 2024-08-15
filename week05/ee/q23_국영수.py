# 국영수
import sys
sys.stdin = open("q23_input.txt")
N = int(input())

students = []
for _ in range(N):
    students.append(input().split())

students.sort(key=lambda x: x[0])
students.sort(reverse=True, key=lambda x: int(x[3]))
students.sort(key=lambda x: int(x[2]))
students.sort(reverse=True, key=lambda x: int(x[1]))

for student in students:
    print(student[0])

