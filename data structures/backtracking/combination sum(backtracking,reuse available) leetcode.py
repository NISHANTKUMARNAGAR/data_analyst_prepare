class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 1:  # if only 1 element in candidates
            if candidates[0] == target:
                return [[candidates[0]]]
            else:
                return []
        final = []
        candidates.sort()  # as orignal list might not be sorted

        def calcsum(remsum, pointer, choice):
            if remsum == 0:
                final.append(choice[:])  # choice[:] is copy of current data in choice as choice changes many times
                return
            for i in range(pointer, len(candidates)):
                if candidates[
                    i] > remsum:  # if current item is greater than remsum no point in continue so we go no further
                    return
                # make choice
                remsum = remsum - candidates[i]
                choice.append(candidates[i])
                # go deeper
                calcsum(remsum, i,
                        choice)  # we use i not i+1 or 0 as duplicates allowed so can choose value at same index twice
                # undo choice
                choice.pop()
                remsum = remsum + candidates[i]

        calcsum(target, 0, [])
        # 1st parameter is target sum to be aechieved
        # 2nd parameter is pointer pointing to current index in current recursion
        # 3rd parameter is group of choosen elements
        return final