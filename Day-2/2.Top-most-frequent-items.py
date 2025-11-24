from typing import List

# using hash map and sorting

def topKFrequent( nums: List[int], k: int) -> List[int]:
    items= dict()
    for n in nums:
        if n in items:
            items[n] += 1
        else:
            items[n] = 1
    sorted_items = sorted(items.items(), key=lambda x: x[1], reverse=True)
    result = []
    for i in range(k):
        result.append(sorted_items[i][0])
    return result


# using bucket sort
def topKFrequent2( nums: List[int], k: int) -> List[int]:
    items= dict()
    for n in nums:
        if n in items:
            items[n] += 1
        else:
            items[n] = 1
    
    bucket = [[] for _ in range(len(nums) + 1)]
    print(items.items())
    for num, freq in items.items():
        print(num, freq)
        bucket[freq].append(num)
    
    print(bucket)
    result = []
    for i in range(len(bucket) - 1, 0, -1):
        for n in bucket[i]:
            print(bucket[i])
            print(n)
            result.append(n)
            if len(result) == k:
                return result
    return result
print(topKFrequent2([1,1,1,2,2,3], 2))  # Output: [1, 2]