from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)

        if endWord not in words:
            return 0

        q = deque([(beginWord, 1)])
        words.discard(beginWord)

        while q:
            word, length = q.popleft()

            if word == endWord:
                return length
            
            for i in range(len(word)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + char + word[i+1:]

                    if new_word in words:
                        words.remove(new_word)
                        q.append((new_word, length + 1))
        return 0