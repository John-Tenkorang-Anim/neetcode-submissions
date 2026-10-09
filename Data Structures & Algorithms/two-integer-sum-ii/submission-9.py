class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        count = {}

        for index, value in enumerate(numbers, start = 1):
            diff = target - value
            if diff in count:
                return [count[diff], index]
            count[value] = index



        