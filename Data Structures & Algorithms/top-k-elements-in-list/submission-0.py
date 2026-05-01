class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get counter to count the occurrences of the number
        # get all values in reversed list
        # for every number of times that we want to go, we get the key for the highest
        from collections import Counter
        counter = Counter(nums)
        return [num for num, freq in sorted(counter.items(), key=lambda x: x[1], reverse=True)[:k]]
        