class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        farthest = 0
        current_position = 0
        for i in range(len(nums)):
            if current_position == len(nums)-1:
                return jump
            farthest = max(farthest, i + nums[i])
            if i == current_position:
                jump += 1
                current_position = farthest
        return jump