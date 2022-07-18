#
# @lc app=leetcode.cn id=30 lang=python
#
# [30] 串联所有单词的子串
#

# @lc code=start
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []

        wordsMap = {}
        statisticsMap = {}
        wordsCount = 0
        statisticsWordsCount = 0
        
        for word in words:
            wordsCount += 1
            if wordsMap.get(word):
                wordsMap[word] += 1
            else:
                wordsMap[word] = 1
        wordLen = len(words[0])
        for i in range(wordLen):
            for key in wordsMap:
                statisticsMap[key] = 0
            statisticsWordsCount = 0
            while i < len(s):
                # TODO
                currentWord = s[i:i+wordLen]
                if currentWord in wordsMap:
                    statisticsMap[currentWord] += 1
                    statisticsWordsCount += 1
                    
                    while statisticsMap[currentWord] > wordsMap[currentWord]:
                        start = i - (statisticsWordsCount-1)*wordLen
                        startWord = s[start:start+wordLen]
                        statisticsMap[startWord] -= 1
                        statisticsWordsCount -= 1
                    
                    if statisticsWordsCount == wordsCount:
                        start = i - (statisticsWordsCount-1)*wordLen
                        res.append(start)
                    
                else:
                    for key in wordsMap:
                        statisticsMap[key] = 0
                    statisticsWordsCount = 0

                i += wordLen
        return res
        
                
# @lc code=end

# Solution().findSubstring("barfoothefoobarman", ["foo","bar"])

