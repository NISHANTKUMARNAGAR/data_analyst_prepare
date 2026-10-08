#move max possible currently,if higher jump chance discovered take that:-
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i=0
        while i<len(nums):
            if i==len(nums)-1: #if at last index
                return True
            elif nums[i]==0: #if at 0 value
                return False
            else:
                temp=nums[i]
                for j in range(1,temp+1):
                    #move the steps at value i,if nums[i]>remaining steps,or you reached end then great break loop use that i
                    i=i+1
                    if i<len(nums): #if i is not after end of list
                        if nums[i]>temp-j or i==len(nums)-1:
                            break