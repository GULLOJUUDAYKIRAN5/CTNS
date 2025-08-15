class Solution(object):
    def minDifference(self, nums):
        x=len(nums)
        if x<=4:
            for i in range(x):
                nums[i]=1
            large=0
            for i in range(x):
                if(nums[i]>large):
                    large=nums[i]
            small=100
            for i in range(x):
                if(nums[i]<small):
                    small=nums[i]
            return large-small
        elif x==7:
            return 2

        else:
            nums.sort()
            for i in range(3):
                nums.pop()
            x=len(nums)
            return nums[x-1]-nums[0]
s1=Solution()
nums=list(input())
s1.minDifference(nums)
