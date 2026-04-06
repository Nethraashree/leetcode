class Solution:
    def rob(self, nums):
        prev2 = 0   
        prev1 = 0   
        for num in nums:
            current = max(num + prev2, prev1)
            prev2 = prev1
            prev1 = current

        return prev1