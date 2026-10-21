from collections import Counter, deque
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = Counter(nums)
        temp = []
        for key, value in nums.most_common(k):
            temp.append(key)
 
        return temp

        
