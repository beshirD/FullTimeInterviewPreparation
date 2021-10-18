#
# @lc app=leetcode id=1423 lang=python
#
# [1423] Maximum Points You Can Obtain from Cards
#

# @lc code=start
class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        total_sum = sum(cardPoints)
        n = len(cardPoints)
        prefix_sum = [cardPoints[0]]
        i = 0
        j = len(cardPoints) - k
        
        for i in range(1,len(cardPoints)):
            prefix_sum.append(prefix_sum[i-1] + cardPoints[i])
       
        answer = total_sum - prefix_sum[n-k-1]
        i = 0 
        j = n - k
        while j < n:
            answer = max(answer,total_sum - (prefix_sum[j] - prefix_sum[i]))
            i += 1
            j += 1
        return answer
            
            
# @lc code=end

