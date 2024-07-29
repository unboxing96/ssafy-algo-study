# 모르겠어요


# from copy import deepcopy

# def solution(key, lock):
#     M = len(key)
#     N = len(lock)

#     # 행돌
#     def rotation(matrix, N):
#         result = [[0 for i in range(N)] for i in range(N)]

#         for i in range(len(matrix)):
#             for j in range(len(matrix)):
#                 result[i][j] = matrix[N-1-j][i]

#         return result
    
#     # 행렬 세트화
#     def make_set(matrix):
#         res = set()
#         for row in matrix:
#             res.update(set(row))
#         return res
    
#     rotated_key = deepcopy(key)    
    
#     # 열쇠+키 확인
#     for _ in range(4):
#         for i in range(N+M-1):
#             for j in range(N+M-1):
#                 # 행렬 복사
                
#                 copied_lock = deepcopy(lock)

#                 for k in range(N+M-i-1):
#                     for l in range(N+M-j-1):
#                         if 0<=k-1<N and 0<=l-1<N and 0<=N+M-k-1<M and 0<=N+M-l-1<M:
#                             copied_lock[k-1][l-1] += rotated_key[N+M-k-1][N+M-l-1]

#                 for _ in copied_lock:
#                     print(_)

#                 print('--------')
#                 if make_set(copied_lock) == {1}:
#                     return True
                
#         rotated_key = rotation(rotated_key, M)
        
                
    # return False


# key = [
#     [1, 2, 3],
#     [1, 1, 1],
#     [1, 1, 1]
# ]
# lock = [
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0]
# ]



# print(solution(key, lock))

# mtrx = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]


# [[13, 9, 5, 1], 
#  [14, 10, 6, 2], 
#  [15, 11, 7, 3],
#  [16, 12, 8, 4]
#  ]



# N = len(mtrx)

# k = [[0 for i in range(N)] for i in range(N)]


# for i in range(len(mtrx)):
#     for j in range(len(mtrx)):
#         k[i][j] = mtrx[N-1-j][i]

# print(k)




# print(make_set(key))
