class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Two pointers require sorted array
        final = []

        # We only go till len(nums) - 2 because we need 3 numbers
        for i in range(len(nums) - 2):

            # Skip duplicate values for the outer loop
            # If current value is same as previous, skip it
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Now we fix nums[i] and try to find two numbers
            # whose sum + nums[i] equals 0
            left = i + 1
            right = len(nums) - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    # Need bigger sum → move left pointer right
                    left += 1

                elif total > 0:
                    # Need smaller sum → move right pointer left
                    right -= 1

                else:
                    # Found a valid triplet
                    final.append([nums[i], nums[left], nums[right]])

                    # Move both pointers
                    left += 1
                    right -= 1

                    # Skip duplicates on left side
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicates on right side
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return final
