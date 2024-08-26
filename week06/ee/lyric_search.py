#프로그래머스 60060 가사 검색
# 4일차 가사검색 문제의 효율성 테스트에서 막히면 Trie 자료구조에 대해 학습해 보세요.

# ah yeah 못하겠습니다.
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.word = False #단어가 끝났는지
        self.children = defaultdict(TrieNode) #새로운 문자가 발견될 때마다 새로운 TrieNode 객체 생성

class Trie:
    def __init__(self):
        self.root = TrieNode()

    #단어 삽입
    def insert(self, word):
        node = self.root
        for char in word: #단어의 각 문자들을 순서대로 확인
            node = node.children[char]
        node.word = True

    #단어 존재 여부 판별
    def search(self, query):

        if query[0] == '?': # '?'가 접두사인 경우
            for char in query:
                if char == '?':
                    pass
                #어떡하ㅏ난요~!~!~!~!~!~!?????~~?!~~>!?~>!몰라욤ㄹ몰ㅇ아료


        else: # '?'가 접미사인 경우
            node = self.root

            for char in query:

                if char == '?':
                    pass #어케 해야됨?
                elif char in node.children:
                    node = node.children[char]
                else: # 노드에 없으면
                    return 0

                if node.word: #단어 끝났으면
                    return 0

            else:
                return 1


def solution(words, queries):
    answer = []
    trie = Trie()

    # 이분탐색을 어따 쓰냐고~~~~~~~~~~~~~~~

    for word in words:
        trie.insert(word)

    for query in queries:
        trie.search(query)

    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
["fro??", "????o", "fr???", "fro???", "pro?"])) #[3, 2, 4, 1, 0]
