from typing import List

# hashMap approach

def containsDuplicate(nums: List[int]) -> bool:
    dup = dict()
    for i in range(len(nums)):
        if nums[i] in dup:
            dup[nums[i]] += 1
            return True
        else:
            dup[nums[i]] = 1
    
    return False

# set approach
def containsDuplicate2(nums: List[int]) -> bool:
    dup = set()
    for i in nums:
        if i in dup:
            return True
        else:
            dup.add(i)
    
    return False

print(containsDuplicate([1,2,3,4]))
print(containsDuplicate2([1,2,3,4]))


