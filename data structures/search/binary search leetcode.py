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

#modified binary search on sorted left sorted array
#meaning the array has now two half sorted array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # default binary search
        def binarysearch(l, r):
            while (l <= r):
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1

            return -1

        # if sorted array
        if nums[0] <= nums[len(nums) - 1]:
            left = 0
            right = len(nums) - 1
            final = binarysearch(left, right)
            return final
        # rotated sorted array
        else:
            # we find pivot or rotation point(r) where nums[r] is smallest value
            # modified binary search for list with two sorted subsets
            l, r = 0, len(nums) - 1
            while (l <= r):
                m = (l + r) // 2
                if nums[m] < nums[m + 1] and nums[m] < nums[m - 1]:  # value  at index is smallest
                    r = m
                    break
                elif nums[m] > nums[m + 1] and nums[m] > nums[m - 1]:  # value at index is biggest
                    r = m + 1
                    break
                elif nums[m] > nums[0]:  # we are in biggger subset move left
                    l = m + 1
                else:  # we are in smaller subset move right
                    r = m - 1

            # after finding r we apply binarysearch in proper subset
            if target >= nums[0]:  # target is in bigger subset
                left = 0
                right = r - 1
            else:  # target<l[0] is in smaller subset
                left = r
                right = len(nums) - 1
            final = binarysearch(left, right)
            return final

#koko eating banana
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