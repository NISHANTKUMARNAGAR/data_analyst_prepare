#combination sum part 1
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

#combination sum part 2
#input list can have multiple values used set to solve and used it around
#used i+1 in backtracking step to not use same value
#did not put a separate condition if length is 1 as inner function handles that also
class Solution:
    def combinationSum2(self,candidates,target):
        result = []
        candidates.sort()

        def gencomb(remsum, curr, comb):
            if remsum == 0:
                result.append(comb[:])
                return

            seen = set()
            for i in range(curr, len(candidates)):
                if candidates[i] > remsum: #stop if current candidate > remaining sum will not take this value so we return
                    return
                if  candidates[i] in seen: #skip this value as another index value with same magnitude is used in same loop
                    continue
                seen.add(candidates[i])
                remsum = remsum - candidates[i]
                comb.append(candidates[i])
                gencomb(remsum, i + 1, comb)
                comb.pop()
                remsum = remsum + candidates[i]
            seen.clear()

        gencomb(target, 0, [])
        return result

o=Solution()
print(o.combinationSum2([10,1,2,7,6,1,5],8))
#[1,1,2,5,6,7,10]
#[[1,1,6],[1,2,5],[1,7],[2,6]]

# Unlike Combination Sum I, each candidate can be used only once, so recursion
# advances to i + 1. Sorting allows early termination when a candidate exceeds
# remsum. A set at each recursion level skips duplicate values at that level,
# preventing duplicate combinations while still allowing equal values at
# different indices to appear together in a combination.
#
# I use a set named `seen` to prevent duplicate combinations caused by
# repeated candidate values. I declare `seen = set()` inside `gencomb()`,
# before the for loop, so that every recursive call gets its own set.
# This is important because duplicates should be skipped only at the
# current recursion level, not across different levels of the recursion.
#
# Inside the loop, `if candidates[i] in seen` checks whether the current
# candidate value has already been considered at this recursion level.
# If it has, `continue` skips that occurrence and moves to the next
# candidate, avoiding duplicate combinations.
#
# If the value has not been encountered at this level, `seen.add(candidates[i])`
# records it so that any subsequent occurrence of the same value at this
# level will be skipped.
#
# I use `seen.clear()` after the loop to empty the set. Since `seen` is
# local to this function call and is discarded when the call finishes,
# clearing it is not necessary for correctness; it simply makes the
# intention to clear the set explicit.
#
# Unlike Combination Sum I, each candidate occurrence can be used only
# once, so the recursive call uses `i + 1`. Sorting the candidates also
# lets me stop exploring when a candidate exceeds the remaining sum.
#
#set is only cleared when current loop ends in a loop it would not use same magnitude value at different indexes
#thats why its clear after loop ends