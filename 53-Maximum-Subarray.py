class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        curent_sum=0
        for num in nums:
            curent_sum += num

            max_sum = max(max_sum, curent_sum)

            if curent_sum < 0:
                curent_sum = 0
            
        return max_sum
        # for i in range(0,len(nums)):
        #     current_sum = nums[i]
        #     if current_sum>max_sum:
        #         max_sum=current_sum

        #     for j in range(i+1,len(nums)):
        #         current_sum=current_sum+nums[j]
        #         if current_sum>max_sum:
        #             max_sum=current_sum
        #return max_sum

        