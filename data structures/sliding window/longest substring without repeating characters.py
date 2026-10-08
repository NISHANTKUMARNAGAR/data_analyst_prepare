#my code (ran in 518 ms)
s="pwwkew"
if (len(s) == 0): #if length 0
    print(0)
elif (len(s) == 1): #if length 1
    print(1)
else:
    length = 0
    start = 0
    end = 0
    checkset = set() #set to check membership
    checkdict = {} #to store index of char.
    while end < len(s):  #till string s lasts
        if s[end] not in checkset: #unique character
            checkset.add(s[end])
            checkdict[s[end]]=end #storing index for adjusting start,end if we find a duplicate char
            if (len(s[start:end+1]) > length): #if till current character substring length>length var.
                length = len(s[start:end+1])
            end = end + 1
        else: #if a reapeated character
            #reset both start,end to skip past duplicate
            start=checkdict[s[end]]+1 #adjusting to just after duplicate character
            end=checkdict[s[end]]+1 ##adjusting to just after duplicate character
            checkset.clear()
    print(length)

#efficient (10ms)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) == 0): #if length 0
            return 0
        elif (len(s) == 1): #if length 1
            return 1
        length = 0
        start = 0
        end = 0
        checkdict = {} #to store index of char., also for membership check
        while end < len(s):  #till string s lasts
            if s[end] not in checkdict: #unique character
                checkdict[s[end]]=end #storing index for adjusting start,end if we find a duplicate char
            else: #if a reapeated character
                #update start to skip past duplicate
                #max() beacuse sometime last seen of repeating char is outside of sliding window
                #thats why we check max(orignal value,last seen of repeating char.) to make sure
                #start never goes backward
                start=max(start,checkdict[s[end]]+1) #set start to max of prev. start and last seen of end
                checkdict[s[end]] = end #update index of repeating character to new location(ie.current loc.)
            #update length everytime the window between start,end is valid
            #and could be when we encounter a duplicate char, or a ounique character
            length=max(length,end-start+1)
            end = end + 1
        return length

#efficient and clear but 14ms
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        start = 0
        end = 0
        checkdict = {}  # to store index of char., also for membership check
        while end < len(s):  # till string s lasts
            if s[end] in checkdict and checkdict[s[end]] >= start:
                # if a reapeated character and last seen of repeated char is after start
                start = checkdict[s[end]] + 1  # update start to skip past duplicate

            checkdict[s[end]] = end  # update index of current character to new location(ie.current loc.)
            # update length everytime if current updated window is bigger or not
            length = max(length, end - start + 1)
            end = end + 1
        return length

"""for last code important points

1. Avoid resetting the sliding window: Don't clear or reset the window. Instead, 
just adjust the start pointer minimally when a duplicate is inside the window.

2. Use a dictionary for membership and index tracking: A dictionary allows O(1) 
membership checks and index updates via hashing, so no need for a set.

3. Use simple math for length: Calculate window length using end - start + 1
 instead of slicing the string, which is more costly.

4. Always move the end pointer forward in each iteration: Never skip the end 
increment; this ensures each character is processed exactly once.

5. Adjust start only when a duplicate is inside the window: Check if the last
 seen index is greater than or equal to start; only then move start forward.

6. Keep a single data structure: Use only one dictionary to track characters
 and their latest indices—no extra structures like sets."""