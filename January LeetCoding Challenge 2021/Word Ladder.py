import queue
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = wordList
        visitedPool = set()
        q = queue.Queue()
        level = 0
        size = 0
        
        q.put(beginWord) #put first word -> beginWord
        visitedPool.add(beginWord)
        for i in words:
            if i == beginWord: words.remove(i)
        print(words)
        #BFS
        while not q.empty():
            # queue is not empty
            size = q.qsize()
            
            level += 1
            print("Level",level)
            while size>0:
                currentWord = q.get()
                if currentWord == endWord: 
                    print(words)
                    print(currentWord)
                    return level
                allWordsSet = self.allWords(currentWord)
                needToRemove = list()
                for wordsItem in words:
                    if wordsItem in allWordsSet and wordsItem not in visitedPool:
                        print("remove wordsItem", wordsItem)
                        # words.remove(wordsItem)
                        needToRemove.append(wordsItem)
                        visitedPool.add(wordsItem)
                        q.put(wordsItem)
                for needToR in needToRemove:
                    words.remove(needToR)
                size -= 1
        return 0
            
            
            
    def allWords(self, currentWord):
        finishList = set()
        for i in range(len(currentWord)):
            temp = currentWord
            for asciiNo in range(97,123):
                temp = temp[:i] + chr(asciiNo) + temp[i+1:]
                finishList.add(temp)
        return finishList
        
        
        
# Hard
# BFS