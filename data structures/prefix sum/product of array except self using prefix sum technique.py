class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixarr = [1]
        prefixtemp = 1
        for i in range(len(nums)):  # calcuate product till just prev. number to create prefix array
            if (i > 0):
                prefixtemp = prefixtemp * nums[i - 1]  # multiplying with just prev. value to temp
                prefixarr.append(prefixtemp)  # store that temp value to prefix array

        suffixarr = [1]
        suffixtemp = 1
        for j in range(
                len(nums) - 1):  # doing same as above just for suffix array and len(nums)-i to getreversed values
            # did not use if like above because already did len(nums)-1 above
            suffixtemp = suffixtemp * nums[len(nums) - (j + 1)]
            suffixarr.append(suffixtemp)
        suffixarr.reverse()

        final = []
        for k in range(len(nums)):  # combining preoduct of prefixarr and suffixarr
            final.append(prefixarr[k] * suffixarr[k])

        return final