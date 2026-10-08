import xml.etree.ElementTree as et
tree=et.parse("depthtest.xml")
root=tree.getroot()
maxdepth=0

def finddepth(node,level):
    global maxdepth
    if(level>maxdepth):
        maxdepth=level
    for child in node:
        finddepth(child,level+1)

finddepth(root,-1)
print(maxdepth)
######WHY THIS WORKS-------------------------------------------
# so we increase level/depth when we go into a child and its diff.
# from brefore "maxdepth=maxdepth+1" as then it would
# increse depth when loop runs for every new sibling which was
# wrong ,and we wanted to increase depth when new deeper level
# or inner child was encountered and also we only incerase
# max depth when level of this child is deeper then before
# thats why in our example depthtest.xml when we increased to level 5
# on fifthchild deep inside 'subtitle' it set level to 5 and as it
# was greater then any before it updated maxdepth to 5 and also
# as 5 would be greater than any other depth inside depthtest.xml,it
# would not allow to update maxdepth again because of
# if(level>maxdepth),also if any node has no children loop would
# not run and this version of function would end with only with
# updating if this level would be greater than before
#####WHY PREVIOUS .ITER FAILED---------------------------------
# In the previous code you used .iter() to find children.
# But .iter() returns ALL descendants (children, grandchildren, etc.)
# at once,so you were not moving one level at a time — you were
# jumping through the whole subtree.You increased maxdepth for EVERY
# child encountered,which counted the total number of nodes instead
# of how many levels exist.More siblings falsely increased depth,
# even though they were at the same level.Because .iter() was
# returning grandchildren directly from a parent, recursion was
# called multiple times on the same nodes, creating repeated visits
# and completely losing the level structure.
#####WHY THIS IS BETTER THAN USING RETRURN---------------------
# Checking the level BEFORE the for-loop is simpler because:We update
# maxdepth immediately when we go one level deeper.We do not need
# to return anything from recursion.We do not need to store or
# compare depths of every child manually.Recursion only moves depth
# downward; no value needs to travel back upward. Taking a return
# value from each recursive call and comparing it INSIDE the loop is
# more complex because,Every recursive call must return a depth
# value to its parent.The parent must receive that value, store it,
# and compare it for every child.We must track the maximum of all
# returned values inside the loop.We must return a depth again
# after finishing the loop to the previous caller.In other words,
# depth must be passed back up through every level of recursion,which
# makes the logic more complicated to write and easier to get wrong.
# So the current approach is simpler because the depth is tracked on
# the way DOWN (using 'level' and updating maxdepth immediately),
# while the alternative approach tracks depth on the way BACK UP,
# which requires extra comparisons, variables, and returns.

""""if root starts at -1 according to hackerrank"""
"""
import xml.etree.ElementTree as etree
maxdepth=0

def depth(elem, level):
    global maxdepth
    level=level+1
    if(level>maxdepth):
        maxdepth=level
    for child in elem:
        depth(child,level)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
"""