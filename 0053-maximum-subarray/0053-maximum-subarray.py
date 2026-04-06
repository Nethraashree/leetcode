class Solution:
    def maxSubArray(self, nums):
        def helper(left, right):
            if left == right:
                return nums[left]

            mid = (left + right) // 2

            
            left_sum = helper(left, mid)
            right_sum = helper(mid + 1, right)

            
            sum_left = float('-inf')
            temp = 0
            for i in range(mid, left - 1, -1):
                temp += nums[i]
                sum_left = max(sum_left, temp)

            sum_right = float('-inf')
            temp = 0
            for i in range(mid + 1, right + 1):
                temp += nums[i]
                sum_right = max(sum_right, temp)

            cross_sum = sum_left + sum_right

            return max(left_sum, right_sum, cross_sum)

        return helper(0, len(nums) - 1)