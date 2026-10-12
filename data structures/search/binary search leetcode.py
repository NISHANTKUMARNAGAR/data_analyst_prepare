#normal binary search on sorted array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        final=len(nums) #becoz final can be btw 0 to len(nums)-1
        left=0
        right=len(nums)-1
        while(left<=right):
            mid=(left+right)//2
            if nums[mid]==target:
                final=mid
                break
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1

        if final<=len(nums)-1: #if final is from 0 to len(nums)-1 any index
            return final
        else:
            return -1


#koko eating banana --- boundary condition question using binary search
#find min,where to use binary search
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        def check(k, h):
            total = 0
            for item in piles:
                total = total + math.ceil(item / k)
            return total <= h  # if total hours to consume<=h then true else False

        # binary search to find optimal eating number using check() function
        # avrange=list(range(1,max(piles)+1))
        # not creating avrange no need
        left = 1
        right = max(piles)  # as right should point to last value in imaginary avrange meaning to index of max(piles)
        while (left < right):
            mid = (left + right) // 2
            if check(mid, h) == True:
                # include mid as it might be correct min banana eating value as its still gave check(mid)=True
                right = mid
            else:
                # exclude mid as its giving false from check
                left = mid + 1

        return left