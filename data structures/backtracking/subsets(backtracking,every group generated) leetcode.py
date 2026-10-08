class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start, path):
            # 1. Add current subset
            res.append(path[:])

            # 2. Explore choices
            for i in range(start, len(nums)):
                path.append(nums[i])  # choose
                backtrack(i + 1, path)  # move forward
                path.pop()  # undo (backtrack)

        backtrack(0, [])
        return res