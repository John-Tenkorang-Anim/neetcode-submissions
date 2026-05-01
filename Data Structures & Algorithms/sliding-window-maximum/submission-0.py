class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        max_sum = []
        right = k
        while right < len(nums) + 1:
            max_sum.append(max(nums[left:right]))
            left += 1
            right += 1
        return max_sum
