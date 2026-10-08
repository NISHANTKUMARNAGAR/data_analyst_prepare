#growing starting from 1st char of 1st item in list::
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(strs[0]!=""): #if list has first value as ""
            if(len(strs)==1): #if only 1 item in list
                return strs[0]
            pre=strs[0][0] #to get initial prefix value as first letter of word at index 0 in list
            j=1 #for looping on items of list
            i=2 #index for getting new prefix value
            while(True):
                item=strs[j]
                if(item.startswith(pre)): #checking every item for prefix
                    if(j==len(strs)-1): #if last item is reached create new pre and update i
                        oldpre=pre #to get previous value of pre to return if new one does not match in any item
                        if(oldpre==strs[0]): #if whole item matches other items i.e. similar items in list like ["ab","ab"]
                            return pre
                        pre=strs[0][0:i] #new value for pre
                        j=1 #to update j to check over in list again
                        i=i+1 #to update value of pre next time
                    else: #when in middle of strs list and this item has prefix
                        j=j+1
                        continue
                else: #prefix not found in current item
                    if(pre==strs[0][0]): #if pre not found at when its only s[0][0]
                        return ""
                    else: #if pre not found at when its more than s[0][0]
                        return oldpre
        else:
            return ""


#shrinking version starts from whole 1st item, decreases when current prefix not found
#until its common in all strings
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""

        return prefix