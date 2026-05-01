class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = len(nums)-1 
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                if  target < nums[l] or nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1