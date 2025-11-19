from typing import List

# brute force approach
def twoSum(nums: List[int], target: int) -> List[int]:
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# using hash map
def twoSum2(nums: List[int], target: int) -> List[int]:
    num_map = dict()
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in num_map:
            return [num_map[diff], i]
        num_map[nums[i]] = i


print(twoSum3([3,7,6,15], 13))