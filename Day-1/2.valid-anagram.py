
# brute force approach
def isAnagram(s: str, t: str) -> bool:
    s = sorted(s)
    t = sorted(t)
    return s == t

# hashMap approach
def isAnagram2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    countS = dict()
    countT = dict()
    
    for i in range(len(s)):
        if s[i] in countS:
            countS[s[i]] += 1
        else:
            countS[s[i]] = 1
        
        if t[i] in countT:
            countT[t[i]] += 1
        else:
            countT[t[i]] = 1

    return countS == countT
print(isAnagram2("anagram", "nagaram"))
