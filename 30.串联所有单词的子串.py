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
        wordsMap = {}
        statisticsMap = {}
        for word in words:
            if wordsMap.get(word):
                wordsMap[word] = wordsMap[word] + 1
            else:
                wordsMap[word] = 0
                statisticsMap[word] = 0
        wordLen = len(words[0])
        for i in range(0, len(s), wordLen):
            # TODO
            pass

    def wordCompare(word, s, index):
        wordLen = len(word)
        for i in range(index, index+wordLen):
            if s[i] != word[i]:
                return False
        return True
        
                
# @lc code=end

