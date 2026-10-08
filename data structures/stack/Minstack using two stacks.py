#unoptimized but working
"""class MinStack:
    def __init__(self):
        self.stack = []  # to store all elements
        self.stackmin = []  # to keep track of min according to number of elements by index
        self.currentmin = 2 ** 31  # var to compare every new elemnt to find which is min

    def push(self, val: int) -> None:
        self.stack.append(val)  # just add to stack
        if not self.stackmin:  # if stackmin empty
            self.stackmin.append(val)  # just append the current val as its obv the min val because number of ele=1
            self.currentmin = val  # put this val as currentmin
        else:  # if stackmin not empty
            if val < self.currentmin:  # compare if pushed val is less than currentmin
                self.stackmin.append(val)  # if yes then add it to stackmin as this is min val from all pushed ele.
                self.currentmin = val  # update the currentmin
            else:  # if val is not lesser than current min(works if val is greater or equal to)
                self.stackmin.append(self.currentmin)  # we just add currnetmin to stackmin and dont change currentmin

    def pop(self) -> None:
        self.stack.pop()  # just remove the element
        # now it does not matter if the popped value is current min val or not as if it is now it gets
        # removed from the stack or if its not current min value and its a larger value again removing it
        # does not affect stackmin as it stores min value according to number of elements present and since
        # its a large value and poped from top of stack or end of list stack it does not change the currnemin
        # variable or the stackmin list so ,,,in both cases we just remove the top value of stackmin list as
        # now the number of elements in the stack list is decreased and also we change the value of the
        # currnetmin variable as now the min. value would be the value at the top of stackmin as that is number
        # of the elements there are currnetly present in the stack
        self.stackmin.pop()
        if not self.stackmin and not self.stack:
            self.currentmin = 2 ** 31  # if stackmin,stack gets empty reassign currentmin to orignal value
        else:
            self.currentmin = self.stackmin[-1]  # assigning the value at top of stackmin to currentmin variable

    def top(self) -> int:
        return self.stack[-1]  # just giving back the value at top of stack list

    def getMin(self) -> int:
        return self.currentmin  # just giving back the value at top of stackmin list
        # also we dont need to change or pop or push any value here as getMin() is just supposed to
        # give back the value that is min currently

    # the stackmin is just to keep track of current min value according to how many elements there are in
    # stack ex. if there are 5 elements currnetly and lets say we remove from top, now there 4 elements
    # so we need the value of currnetmin that was at the time before there were only 4 elements so there the
    # stackmnin list helps i.e. we can assign currentmin=stackmin[len(stackmin)-1] i.e. value at top of
    # stackmin ,,,also if add any element we just see if pushed value is smaller that becomes the currnetmin
    # if not currnetmin stays same, so by this we keep all operations in O(1) by not doing any sorting or
    # whatever by just keeping track of current min as we go on

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
"""

#optimized
"""class MinStack:

    def __init__(self):
        self.stack = []  # to store all elements
        self.stackmin = []  # to keep track of min according to number of elements by index

    def push(self, val: int) -> None:
        self.stack.append(val)  # just add to stack
        if not self.stackmin:  # if stackmin empty
            self.stackmin.append(val)  # just append the current val as its obv the min val because number of ele=1
        else:  # if stackmin not empty
            if val < self.stackmin[-1]:  # compare if pushed val is less than top of stackmin i.e. current min.
                self.stackmin.append(val)  # if yes then add it to stackmin as this is min val from all pushed ele.
            else:  # if val is not lesser than current min.(works if val is greater or equal to)
                self.stackmin.append(self.stackmin[-1])  # we just add current min. i.e. top of stackmin

    def pop(self) -> None:
        self.stack.pop()  # just remove the element
        # now it does not matter if the popped value is current min val or not as if it is now it gets
        # removed from the stack or if its not current min value and its a larger value again removing it
        # does not affect stackmin as it stores min value according to number of elements present and since
        # its a large value and poped from top of stack or end of list stack it does not change the current min.
        # variable or the stackmin list so ,,,in both cases we just remove the top value of stackmin list as
        # now the number of elements in the stack list is decreased
        self.stackmin.pop()

    def top(self) -> int:
        return self.stack[-1]  # just giving back the value at top of stack list

    def getMin(self) -> int:
        return self.stackmin[-1]  # just giving back the value at top of stackmin list
        # also we dont need to change or pop or push any value here as getMin() is just supposed to
        # give back the value that is min currently

    # the stackmin is just to keep track of current min value according to how many elements there are in
    # stack ex. if there are 5 elements currnetly and lets say we remove from top, now there 4 elements
    # so we need the value of currnetmin that was at the time before there were only 4 elements so there the
    # stackmnin list helps i.e. we can assign currentmin=stackmin[len(stackmin)-1] i.e. value at top of
    # stackmin ,,,also if add any element we just see if pushed value is smaller that becomes the currnetmin
    # if not currnetmin stays same, so by this we keep all operations in O(1) by not doing any sorting or
    # whatever by just keeping track of current min as we go on

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
"""