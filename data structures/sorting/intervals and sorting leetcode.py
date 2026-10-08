#merge all overlapping intervals:-
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        final=[]
        intervals.sort()
        #lower will always be lower than upper by default
        lower=intervals[0][0]
        upper=intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]<lower:
                #if new groups 1st val. is less than lower,update lower
                lower=intervals[i][0]
                if intervals[i][1]>upper:
                #if 1st<lower and 2nd>upper this group includes current lower,upper just update thedm
                    upper=intervals[i][1]
            elif intervals[i][0]<=upper and intervals[i][1]>upper: #2nd>bigger
                upper=intervals[i][1]
            elif intervals[i][0]>upper:
                #if entirely new range i.e 1st>upper
                final.append([lower,upper])
                lower=intervals[i][0]
                upper=intervals[i][1]
        final.append([lower,upper]) #for last remaining group
        return final

#remove minimum overlapping intervals find that number:-
#way is to find overlapping then select the interval that ends first take that and free space for new intervals
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        remove=0
        intervals.sort()
        #lower will always be lower than upper by default
        upper=intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]<upper: #all intersecting cases
                if upper>intervals[i][1]: #we pick lower range to keep max non-overlapping
                    upper=intervals[i][1]
                remove=remove+1
            elif intervals[i][0]>=upper:
                #if entirely new range
                upper=intervals[i][1]
        return remove

#find min arrows to burst ballons:-
#way is find the common x to shoot i.e. keep ttrack of currentsmallestupper and make group decide number of arrows
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrow = 0
        i = 1
        currentsmallestupper = points[0][1]
        while i < len(points):
            if points[i][0] <= currentsmallestupper:  # overlaps with group having currentsmallestupper
                if points[i][
                    1] < currentsmallestupper:  # if new group's upper bound is smaller than currentsmallestupper
                    currentsmallestupper = points[i][1]
            else:  # doesnt overlapp
                arrow = arrow + 1  # means 1 arrow for before which ones overlapped
                currentsmallestupper = points[i][1]  # now this points[i] is current smallest
            i = i + 1

        # 1 extra arrow for last of overlapping ballons
        return arrow + 1

        # [[0, 9], [1, 6], [1, 8], [6, 9], [6, 11], [7, 8], [7, 10], [7, 13], [9, 13], [9, 16]]