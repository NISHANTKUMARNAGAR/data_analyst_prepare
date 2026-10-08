class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final=[]
        pool=nums.copy()

        def permu(pointer,choice):
            if(len(choice)==len(nums)):
                final.append(choice[:])
            for i in range(len(pool)): #but when we choose from pool we choose new index each time using loop
                # choose
                choice.append(pool[i])
                temp=pool.pop(i)
                # move forward
                permu(0,choice) #when we move into the choice i.e. go deeper we choose 1st index i.e. index=0
                # undo (backtrack)
                choice.pop()
                pool.insert(i,temp)

        permu(0,[])
        return final