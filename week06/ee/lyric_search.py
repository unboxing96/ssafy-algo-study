#프로그래머스 60060 가사 검색

# 쿼리와 일치하는 단어 개수를 세는 것
# = 쿼리와 일치하는 가장 왼쪽 단어 인덱스와 가장 오른쪽 단어 인덱스 차이를 구하는 것

def binary_search(words, target):
    left = 0
    right = len(words)
    # print(words)
    # print(target)
    while left < right:
        mid = (left + right) //2
        if target < words[mid]:
            right = mid
        elif target > words[mid]:
            left = mid + 1
        else:
            return mid
    return right

def solution(words, queries):
    answer = []
    # words의 길이(가사 단어의 개수)는 2 이상 100,000 이하입니다.
    # 가사에 동일 단어가 여러 번 나올 경우 중복을 제거하고 words에는 하나로만 제공됩니다.
    words.sort()
    # print(words)

    words_group = [[] for _ in range(100000)]
    reversed_words_group = [[] for _ in range(100000)]

    for word in words:
        words_group[len(word)].append(word)
        reversed_words_group[len(word)].append(word[::-1])
        # reversed_words_group[len(word)].sort()
    for group in reversed_words_group:
        group.sort()
    # print(reversed_words_group)
    # # 거꾸로 뒤집은 words 만들기
    # reverse_words = []
    # for word in words:
    #     reverse_words.append(word[::-1])
    # print(reverse_words)

    for query in queries:
        temp = 0
        querya = query.replace("?", "a")
        queryz = query.replace("?", "z")

        # print(querya, queryz)

        if query[0] != '?': # '?'가 접미사일때
            # print(binary_search(words_group[len(query)], queryz))
            # print(binary_search(words_group[len(query)], querya))
            temp = binary_search(words_group[len(query)], queryz) \
                   - binary_search(words_group[len(query)], querya)
        else: # '?'가 접두사일때
            # print(binary_search(reversed_words_group[len(query)], queryz[::-1]))
            # print(binary_search(reversed_words_group[len(query)], querya[::-1]))
            temp = binary_search(reversed_words_group[len(query)], queryz[::-1]) \
                   - binary_search(reversed_words_group[len(query)], querya[::-1])

        answer.append(temp)

    return answer


##########################################################################

# def check(word, query):
#     if len(word) != len(query):
#         return False
#
#     for i in range(len(word)):
#         if word[i] == query[i]:
#             continue
#         elif query[i] == '?':
#             continue
#         elif word[i] != query[i]:
#             return False
#
#     return True
#
# def solution(words, queries):
#     answer = []
#
#     for query in queries:
#         count = 0
#         for word in words:
#             if check(word, query):
#                 count += 1
#         answer.append(count)
#
#     return answer
#
#

#################################################################################

# from collections import defaultdict
#
# class TrieNode:
#     def __init__(self):
#         self.word = False #단어가 끝났는지
#         self.children = defaultdict(TrieNode) #새로운 문자가 발견될 때마다 새로운 TrieNode 객체 생성
#
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
#
#     #단어 삽입
#     def insert(self, word: str) -> None:
#         node = self.root
#         for char in word: #단어의 각 문자들을 순서대로 확인
#             node = node.children[char]
#         node.word = True
#
#     #단어 존재 여부 판별
#     def search(self, query: str)->bool:
#         node = self.root
#         for char in query:
#             if char == '?':
#                 pass
#             elif char in node.children:
#                 node = node.children[char]
#             else:
#                 return 0
#         else:
#             return 1
#
# def solution(words, queries):
#     answer = []
#     trie = Trie()
#
#     # 이분탐색을 어따 쓰냐고~~~~~~~~~~~~~~~
#
#     for word in words:
#         trie.insert(word)
#
#     for query in queries:
#
#
#
#     return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
["fro??", "????o", "fr???", "fro???", "pro?"])) #[3, 2, 4, 1, 0]
