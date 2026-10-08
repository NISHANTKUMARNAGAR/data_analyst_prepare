def twoSum(nums: list[int], target: int) -> list[int]:
    d={}
    for i in range(len(nums)):
        req=target-nums[i]
        if req in d:
            return d[req],i
        else:
            d[nums[i]]=i

nums=[3,4,7,2]
target=6
t=twoSum(nums,target)
print(t)