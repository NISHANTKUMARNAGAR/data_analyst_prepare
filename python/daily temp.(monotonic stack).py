class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:  # if only 1 temp. then cant find warmer temp.
            return [0]

        remtemp = []  # stack to hold indexes for temperatures until we find a warmer temp. for this index's temperature
        answer = len(temperatures) * [0]  # final answer list containing wait times initially wait time for each is 0
        # this remtemp will be a monotonic stack(decreasing) as if we find a big value we just pop the low values(cooler temp.) till a even big value
        # remains by that logic order of elements in remtemp remains decreasing,if we find a lower value we just add its index to remtemp i.e. the
        for i in range(len(temperatures)):
            # stack exists and current temp. is warmer than top of stack,so using while loop we keep going until current temp.
            # is warmer than top of stack and we keep removing and updating wait time to answer list
            while remtemp and temperatures[i] > temperatures[remtemp[-1]]:
                index = remtemp.pop()  # remove top of stack
                answer[index] = i - index  # add wait time to answer list

            # either warmer temp. is found and we popped from stack or not,we add current temp to stack because we need to find
            # warmer temperature for current temperature later
            remtemp.append(i)

            # as we already have wait time 0 by default we dont need to add wait time for remaining indexes in remtemp for which we could not
        # find warmer temperatures for
        return answer