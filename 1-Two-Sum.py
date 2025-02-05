class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has={}
        for i in range(0,len(nums)):
            k=target-nums[i]
            if k in has:
                return [i,has[k]]
            else :
                has[nums[i]]=i
                
