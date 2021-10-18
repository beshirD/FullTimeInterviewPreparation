#
# @lc app=leetcode id=1004 lang=python
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_ones = 0
        count = 0
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] == 1 or k > 0:
                if nums[j] == 0:
                    k -= 1
                j += 1
                count += 1
                max_ones = max(max_ones,count)
            else:
                if nums[i] == 0:
                    k += 1
                count -= 1
                i += 1

        return max_ones   

        
# @lc code=end

