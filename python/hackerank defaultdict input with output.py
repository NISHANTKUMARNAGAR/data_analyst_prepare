#question
# HackerRank "DefaultDict Tutorial":
# First input gives n words for group A and m query words for group B.
# For each word in B, print all 1-based positions where it appears in A;
# if it never appears, print -1.

#answer
#code before suggestion
"""
from collections import defaultdict
n,m=map(int,input().split())

A=[]
for _ in range(n):
    A.append(input())

B=[]
for _ in range(m):
    B.append(input())

final=defaultdict(list)
for i in B:
    found=0
    for j in range(n): #comare B's item with all of A's items
        if(i==A[j]):
            final[i].append(j+1) #B's item key made,position where B's item in A added as value
            found=1
    if(found==0):
        final[i].append(-1)

for position in final.values():
    print(*position,sep=" ") #to unpack position list and " " in between
"""


#code after suggestion
""""
from collections import defaultdict
n,m=map(int,input().split())

#for A group
final=defaultdict(list)
for i in range(n):
    #t is item of A
    t=input()  #while taking A's input create defaultdict with A's keys
    final[t].append(i+1) #in those keys store position

#for B group
for _ in range(m):
    #t2 is item of B
    t2=input()
    if(t2 in final):
        print(*final[t2],sep=" ")
    else:
        print(-1)
"""

#learning
# NOTE: In PyCharm input and output appear mixed in the console,
# but on HackerRank the input is hidden and only your output is
# shown—so printing while reading input never “mixes” with the given input.
