class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=curr_sum=nums[0]
        for i in nums[1:]:
            curr_sum=max(curr_sum+i,i)
            max_sum=max(curr_sum,max_sum)
        return max_sum
s=Solution()
s.maxSubArray([5,4,-1,7,8])
            
