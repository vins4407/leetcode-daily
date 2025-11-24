from typing import List

# group anagrams using hash map
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagram_map = dict()
    
    for s in strs:
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagram_map:
            anagram_map[sorted_s].append(s)
        else:
            anagram_map[sorted_s] = [s]
    
    return list(anagram_map.values())

# 
def groupAnagrams2(strs: List[str]) -> List[List[str]]:
    anagram_map = dict()
    
    for s in strs:
        count = [0] * 26  # assuming only lowercase a-z
        for char in s:
            count[ord(char) - ord('a')] += 1
        # ensure a list exists for this key before appending
        anagram_map.setdefault(tuple(count), []).append(s)
        print(count)
        print(anagram_map)
    return list(anagram_map.values())

print(groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"]))