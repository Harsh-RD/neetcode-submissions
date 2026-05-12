class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,num in enumerate(nums): # enumerate give i, num // dict stores default key value
            complement=target-num
            if complement in seen:
                return [seen[complement],i] # index return
            seen[num]=i # value add to empty dict
