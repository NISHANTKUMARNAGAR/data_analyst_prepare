"""using HEAP------------------------------------------------------------------------------"""
class Solution:
    def topKFrequent(self, nums, k):
        countdict = {}  # to keep frequency count of each distinct item in nums
        for item in nums:
            if item not in countdict:
                countdict[item] = 1
            else:
                countdict[item] = countdict[item] + 1

        from heapq import heappop, heappush
        heap = []  # to get mostfrequent items in form of [freq,key] from dictionary after flipping
        for item in countdict:
            heappush(heap, [-countdict[item], item])

        mostfreq = []  # list of k most frequent items
        for _ in range(k):
            temp = heappop(heap)
            mostfreq.append(temp[1])

        return mostfreq

"""#using BUCKETSORT (bucket based on freq. ranges like b1=freq 1 to 3 etc.)"""
l=[[1,5],[2,3],[4,1],[1,73]] #[frequency,ele]
k=2
#no need for bucket sort if we only have k pairs in l list(if distinct freq/same freq) return keys
#as question never asks for sorting of top freq. items or even if same freq question never asks put them in
#lexographic order
if len(l)==k:
    ans=[]
    for _ in range(k):
        ans.append(l.pop()[1])
    print(ans)

#actual bucket sort
from math import sqrt
nobu=max(1,int(sqrt(max(l)[0]))) #if top freq is very small we dont want nobu=0
finall=[]

def insertion_sort(currbucket):
    newb=[bucket[0]] #sorted bucket list
    for i in range(1,len(currbucket)): #taking every new pair
        f=0
        for j in range(len(newb)): #comparing with sorted and sorting in correct place
            if currbucket[i][0]<newb[j][0] or (currbucket[i][0]==newb[j][0] and currbucket[i][1]>newb[j][1]):
                #if unsorted item(in i) has lesser freq or (equal freq but greater ele) put first
                newb.insert(j,currbucket[i])
                f=1
                break
            elif currbucket[i][0]==newb[j][0] and currbucket[i][1]<newb[j][1]:
                #if unsorted item(in i) has equal freq but lesser ele value pust later
                newb.insert(j+1,currbucket[i])
                f=1
                break
        if f==0:
            #if new unsorted item has freq. greater than any in sorted bucket, put last
            newb.append(currbucket[i])

    finall.extend(newb) #add sorted bucket to final sorted list

#make buckets
bucket=[]
ll=1
ul=nobu
newl=[] #so that not everytime we scan the full topkl we need to just check remaing unprocessed pairs
maxfreq=max(l)[0]
while ll<=maxfreq: #used ll as ul is a derived value,ll is main driving factor and ul is capped later so cant use
    for item in range(len(l)):
        if ul >= l[item][0] >= ll:
            bucket.append(l[item])
        elif l[item][0]>ul:
            newl.append(l[item])
    insertion_sort(bucket)
    ll=ul+1
    ul=ll+nobu-1
    if ul > max(l)[0]:  # if ul exceeds max freq. we have to limit its value
        ul = max(l)[0]
    l=newl.copy() #so usable l shrinks everytime and as newl is list we need to use copy() instead of l=newl
    newl.clear()
    bucket.clear()
    #clear both as new bucket and newtopkl each time for new bucket data

#now finall is the list with top k frequencies sorted we just need to have top 10 items popped and return their key
ans=[]
for _ in range(k):
    ans.append(finall.pop()[1]) #pop take key append to ans
print(ans)
#in bucket sort when selecting bucket size it would be sqrt(max range of items in this case max(freq))
#thats why sqrt(max(topkl)[0])
#and ll for 1st bucket starts from lowest freq ava. and since k=3 so ul=maxfreq-k+1 so 9-3+1 so ll=7

"""#using BUCKETSORT (each freq has its own bucket,just put ele in those bucket from count dict)"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countdict = {}  # to keep frequency count of each distinct item in nums
        for item in nums:
            if item not in countdict:
                countdict[item] = 1
            else:
                countdict[item] = countdict[item] + 1

        freqbuckets = [[] for _ in range(len(nums) + 1)]
        # making len(nums)+1 buckets as that is max no. of freq. possible
        # meaning every index is like a bucket
        for item in countdict:
            freqbuckets[countdict[item]].append(item)
            # add that item to its frequency bucket in freqbucket list

        finalfreqbuckets = []
        for i in range(len(freqbuckets)):
            finalfreqbuckets.extend(freqbuckets[i])

        ans = []  # top k most frequent
        while k > 0:
            ans.append(finalfreqbuckets.pop())
            k = k - 1

        return ans
