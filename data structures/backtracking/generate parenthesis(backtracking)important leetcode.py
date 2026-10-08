class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        final=[]
        def genpar(close,open,group):
            if len(group)==n*2: #only add,if group is of n*2 length i.e. all closing,opening are included
                final.append(group)
                return
            if(open<n): #add opening when they are less than n and go deeper
                group=group+"("
                open=open+1
                genpar(close,open,group)
                open=open-1
                group=group[:-1]
            if(close<open): #add closing when they are less than open as they need to be same
                temp=group
                group=group+")"
                close=close+1
                genpar(close,open,group)
                close=close-1
                group=group[:-1]

        genpar(0,0,"") #recursion function(opening,closing,group)
        return final