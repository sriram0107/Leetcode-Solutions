class Solution(object):
    def maxSubArray(self, nums):
        window = maxWindow = nums[0]
        for num in nums[1:]:
            window = max(num, window + num)
            maxWindow = max(maxWindow, window)
        return maxWindow