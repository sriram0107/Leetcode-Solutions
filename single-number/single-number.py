class Solution(object):
    def singleNumber(self, nums):
        ans = nums[0]
        for i in nums[1:]:
            ans ^= i
        return ans
        