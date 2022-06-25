class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) <= 1:
            return False
        
        hashDict = {}
        for index, value in enumerate(nums):
            
            if value in hashDict:
                prev_value = hashDict[value]
                if index - prev_value <= k:
                    return True
            hashDict[value] = index
        return False