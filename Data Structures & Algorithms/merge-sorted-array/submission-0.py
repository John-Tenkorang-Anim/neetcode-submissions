class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        nums1[m:] = nums2
        print(nums1)

        count =  len(nums1)

        for i in range(len(nums1)):

            min_idx = i

            for j in range(i+1, count ):
                if nums1[j] < nums1[min_idx]:
                    min_idx = j
            
            nums1[i], nums1[min_idx] =  nums1[min_idx], nums1[i]